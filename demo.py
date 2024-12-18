import os
from dataclasses import dataclass

import torch
from peft import LoraConfig
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from trl import SFTTrainer, SFTConfig

from dataset import SFTDataCollator, SFTDataset
from merge import merge_lora_to_base_model
from utils.constants import model2template

# 定义预期列表
valid_base_models = [
    'llama2', 'llama3', 'qwen1.5', 'yi', 'mistral', 'mixtral', 'gemma', 'zephyr', 'phi3', 'qwen2.5'
]

@dataclass
class LoraTrainingArguments:
    per_device_train_batch_size: int
    gradient_accumulation_steps: int
    num_train_epochs: int
    lora_rank: int
    lora_alpha: int
    lora_dropout: int

def extract_base_model(model_id):
    # 提取 base_model 并转换为小写
    base_model = model_id.split('/')[1].split('-')[0].lower()
    return base_model

def validate_base_model(base_model):
    if base_model not in valid_base_models:
        raise ValueError(f"Invalid base_model: {base_model}. Expected one of {valid_base_models}.")

def train_lora(
    model_id: str, context_length: int, training_args: LoraTrainingArguments, revision: str
):
    base_model = extract_base_model(model_id)
    validate_base_model(base_model)
    assert model_id in model2template, f"model_id {model_id} not supported"
    lora_config = LoraConfig(
        r=training_args.lora_rank,
        target_modules=[
            "q_proj",
            "v_proj",
        ],
        lora_alpha=training_args.lora_alpha,
        lora_dropout=training_args.lora_dropout,
        task_type="CAUSAL_LM",
    )

    # Load model in 4-bit to do qLoRA
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
    )

    training_args = SFTConfig(
        per_device_train_batch_size=training_args.per_device_train_batch_size,
        gradient_accumulation_steps=training_args.gradient_accumulation_steps,
        warmup_steps=100,
        learning_rate=2e-4,
        bf16=True,
        logging_steps=20,
        output_dir="outputs",
        optim="paged_adamw_8bit",
        remove_unused_columns=False,
        num_train_epochs=training_args.num_train_epochs,
        max_seq_length=context_length,
    )
    tokenizer = AutoTokenizer.from_pretrained(
        model_id,
        use_fast=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=bnb_config,
        device_map={"": 0},
        token=os.environ["HF_TOKEN"],
        revision=revision,
    )

    # Load dataset
    dataset = SFTDataset(
        file="demo_data.jsonl",
        tokenizer=tokenizer,
        max_seq_length=context_length,
        template=model2template[model_id],
    )

    # Define trainer
    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        args=training_args,
        peft_config=lora_config,
        data_collator=SFTDataCollator(tokenizer, max_seq_length=context_length),
    )

    # Train model
    trainer.train()

    # save model
    trainer.save_model("outputs")

    # remove checkpoint folder
    os.system("rm -rf outputs/checkpoint-*")

    # upload lora weights and tokenizer
    print("Training Completed.")

# 确保 model2template 字典包含所有支持的 model_id
model2template = {
    'Qwen/Qwen2.5-3B-Instruct': {
        "system_format": "<s>[SYS]{content}[/SYS]",
        "user_format": "<s>{content}[/USER]",
        "assistant_format": "<s>{content}[/ASSISTANT]",
    },
    'Qwen/Qwen2.5-1.5B-Instruct': {
        "system_format": "<s>[SYS]{content}[/SYS]",
        "user_format": "<s>{content}[/USER]",
        "assistant_format": "<s>{content}[/ASSISTANT]",
    },
    'Qwen/Qwen2.5-3B': {
        "system_format": "<s>[SYS]{content}[/SYS]",
        "user_format": "<s>{content}[/USER]",
        "assistant_format": "<s>{content}[/ASSISTANT]",
    },
    'Qwen/Qwen2.5-1.5B': {
        "system_format": "<s>[SYS]{content}[/SYS]",
        "user_format": "<s>{content}[/USER]",
        "assistant_format": "<s>{content}[/ASSISTANT]",
    },
    # 添加其他模型模板
}

# 调用 train_lora 函数时，确保传入 revision 参数
train_lora(
    model_id="Qwen/Qwen2.5-3B",
    context_length=4096,
    training_args=LoraTrainingArguments(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=8,
        num_train_epochs=3,
        lora_rank=8,
        lora_alpha=16,
        lora_dropout=0.1,
    ),
    revision="main"  # 指定 revision 参数
)
