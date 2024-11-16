model2template = {
    'qwen2.5': {
        "system_format": "<s>[SYS]{content}[/SYS]",
        "user_format": "<s>{content}[/USER]",
        "assistant_format": "<s>{content}[/ASSISTANT]",
    },
    # 添加其他模型模板
}

qwen_template = {
    "system_format": "<|im_start|>system\n{content}<|im_end|>\n",
    "user_format": "<|im_start|>user\n{content}<|im_end|>\n<|im_start|>assistant\n",
    "assistant_format": "{content}<|im_end|>\n",
    "system": "You are a helpful assistant.",
}

gemma_template = {
    "system_format": "<bos>",
    "user_format": "<start_of_turn>user\n{content}<end_of_turn>\n<start_of_turn>model\n",
    "assistant_format": "{content}<|eot_id|>",
    "system": None,
}

yi_template = {
    "system_format": "<|im_start|>system\n{content}<|im_end|>\n",
    "user_format": "<|im_start|>user\n{content}<|im_end|>\n<|im_start|>assistant\n",
    "assistant_format": "{content}<|im_end|>\n",
    "system": None,
}

zephyr_template = {
    "system_format": "<|system|>\n{content}</s>",
    "user_format": "<|user|>\n{content}</s>\n<|assistant|>\n",
    "assistant_format": "{content}</s>\n",
    "system": None,
}

mistral_template = {
    "system_format": "<s>",
    "user_format": "[INST]{content}[/INST]",
    "assistant_format": "{content}</s>",
    "system": "",
}

mixtral_template = {
    "system_format": "<s>",
    "user_format": "[INST]{content}[/INST]",
    "assistant_format": "{content}</s>",
    "system": "",
}

llama2_template = {
    "system_format": "<<SYS>>\n{content}\n<</SYS>>\n\n",
    "user_format": "[INST]{content}[/INST]",
    "assistant_format": "{content} </s>",
    "system": "You are a helpful, respectful and honest assistant. "
    "Always answer as helpfully as possible, while being safe. "
    "Your answers should not include any harmful, unethical, "
    "racist, sexist, toxic, dangerous, or illegal content. "
    "Please ensure that your responses are socially unbiased and positive in nature.\n\n"
    "If a question does not make any sense, or is not factually coherent, "
    "explain why instead of answering something not correct. "
    "If you don't know the answer to a question, please don't share false information.",
}

gemma_template = {
    "system_format": "<bos>",
    "user_format": "<start_of_turn>user\n{content}<end_of_turn>\n<start_of_turn>model\n",
    "assistant_format": "{content}<eos>\n",
    "system": "",
}

llama3_template = {
    "system_format": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{content}<|eot_id|>",
    "user_format": "<|start_header_id|>user<|end_header_id|>\n\n{content}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
    "assistant_format": "{content}<|eot_id|>",
    "system": None,
}



model2template = {
    # Qwen models
    "Qwen/Qwen1.5-0.5B": qwen_template,
    "Qwen/Qwen1.5-0.5B-Chat": qwen_template,
    "Qwen/Qwen1.5-1.8B": qwen_template,
    "Qwen/Qwen1.5-1.8B-Chat": qwen_template,
    "Qwen/Qwen1.5-4B": qwen_template,
    "Qwen/Qwen1.5-4B-Chat": qwen_template,
    "Qwen/Qwen1.5-7B": qwen_template,
    "Qwen/Qwen1.5-7B-Chat": qwen_template,
    "Qwen/Qwen1.5-14B": qwen_template,
    "Qwen/Qwen1.5-14B-Chat": qwen_template,
    "Qwen/Qwen1.5-32B": qwen_template,
    "Qwen/Qwen1.5-32B-Chat": qwen_template,
    "Qwen/Qwen1.5-72B": qwen_template,
    "Qwen/Qwen1.5-72B-Chat": qwen_template,
    "Qwen/Qwen2-0.5B": qwen_template,
    "Qwen/Qwen2-0.5B-Instruct": qwen_template,
    "Qwen/Qwen2-1.5B": qwen_template,
    "Qwen/Qwen2-1.5B-Instruct": qwen_template,
    "Qwen/Qwen2-7B": qwen_template,
    "Qwen/Qwen2-7B-Instruct": qwen_template,
    "Qwen/Qwen2-72B": qwen_template,
    "Qwen/Qwen2-72B-Instruct": qwen_template,
    "Qwen/Qwen2.5-3B":qwen_template,
    # Yi models
    "01-ai/Yi-6B": yi_template,
    "01-ai/Yi-6B-Chat": yi_template,
    "01-ai/Yi-9B": yi_template,
    "01-ai/Yi-9B-Chat": yi_template,
    "01-ai/Yi-34B": yi_template,
    "01-ai/Yi-34B-Chat": yi_template,
    "01-ai/Yi-1.5-6B": yi_template,
    "01-ai/Yi-1.5-6B-Chat": yi_template,
    "01-ai/Yi-1.5-9B": yi_template,
    "01-ai/Yi-1.5-9B-Chat": yi_template,
    "01-ai/Yi-1.5-34B": yi_template,
    "01-ai/Yi-1.5-34B-Chat": yi_template,
    # Mistral models
    "mistralai/Mistral-7B-v0.1": mistral_template,
    "mistralai/Mistral-7B-v0.3": mistral_template,
    "mistralai/Mistral-7B-Instruct-v0.1": mistral_template,
    "mistralai/Mistral-7B-Instruct-v0.2": mistral_template,
    "mistralai/Mistral-7B-Instruct-v0.3": mistral_template,
    # Mixtral models
    "mistralai/Mixtral-8x7B-v0.1": mixtral_template,
    "mistralai/Mixtral-8x7B-Instruct-v0.1": mixtral_template,
    # Gemma models
    "google/gemma-2b": gemma_template,
    "google/gemma-7b": gemma_template,
    "google/gemma-2b-it": gemma_template,
    "google/gemma-7b-it": gemma_template,
    # Zephyr models
    "HuggingFaceH4/zephyr-7b-alpha": zephyr_template,
    "HuggingFaceH4/zephyr-7b-beta": zephyr_template,
    # Llama2 models
    "meta-llama/Llama-2-7b-hf": llama2_template,
    "meta-llama/Llama-2-13b-hf": llama2_template,
    "meta-llama/Llama-2-70b-hf": llama2_template,
    "meta-llama/Llama-2-7b-chat-hf": llama2_template,
    "meta-llama/Llama-2-13b-chat-hf": llama2_template,
    "meta-llama/Llama-2-70b-chat-hf": llama2_template,
    # Llama3 models
    "meta-llama/Meta-Llama-3-8B": llama3_template,
    "meta-llama/Meta-Llama-3-8B-Instruct": llama3_template,
    "meta-llama/Meta-Llama-3-70B": llama3_template,
    "meta-llama/Meta-Llama-3-70B-Instruct": llama3_template,
}

model2size = {
    # Qwen models
    "Qwen/Qwen1.5-0.5B": 620_000_000,
    "Qwen/Qwen1.5-0.5B-Chat": 620_000_000,
    "Qwen/Qwen1.5-1.8B": 1_840_000_000,
    "Qwen/Qwen1.5-1.8B-Chat": 1_840_000_000,
    "Qwen/Qwen1.5-4B": 4_000_000_000,
    "Qwen/Qwen1.5-4B-Chat": 4_000_000_000,
    "Qwen/Qwen1.5-7B": 7_720_000_000,
    "Qwen/Qwen1.5-7B-Chat": 7_720_000_000,
    "Qwen/Qwen1.5-14B": 14_000_000_000,
    "Qwen/Qwen1.5-14B-Chat": 14_000_000_000,
    "Qwen/Qwen1.5-32B": 32_000_000_000,
    "Qwen/Qwen1.5-32B-Chat": 32_000_000_000,
    "Qwen/Qwen1.5-72B": 72_000_000_000,
    "Qwen/Qwen1.5-72B-Chat": 72_000_000_000,
    "Qwen/Qwen2-0.5B": 620_000_000,
    "Qwen/Qwen2-0.5B-Instruct": 620_000_000,
    "Qwen/Qwen2-1.5B": 1_840_000_000,
    "Qwen/Qwen2-1.5B-Instruct": 1_840_000_000,
    "Qwen/Qwen2-7B": 7_720_000_000,
    "Qwen/Qwen2-7B-Instruct": 7_720_000_000,
    "Qwen/Qwen2-72B": 72_000_000_000,
    "Qwen/Qwen2-72B-Instruct": 72_000_000_000,
    "Qwen/Qwen2.5-3B": 3_000_000_000,
    "Qwen/Qwen2.5-3B-Instruct":3_000_000_000,
    # Yi models (estimated sizes)
    "01-ai/Yi-6B": 6_000_000_000,
    "01-ai/Yi-6B-Chat": 6_000_000_000,
    "01-ai/Yi-9B": 8_000_000_000,
    "01-ai/Yi-9B-Chat": 8_000_000_000,
    "01-ai/Yi-34B": 34_000_000_000,
    "01-ai/Yi-34B-Chat": 34_000_000_000,
    "01-ai/Yi-1.5-6B": 6_000_000_000,
    "01-ai/Yi-1.5-6B-Chat": 6_000_000_000,
    "01-ai/Yi-1.5-9B": 8_000_000_000,
    "01-ai/Yi-1.5-9B-Chat": 8_000_000_000,
    "01-ai/Yi-1.5-34B": 34_000_000_000,
    "01-ai/Yi-1.5-34B-Chat": 34_000_000_000,
    # Mistral models
    "mistralai/Mistral-7B-v0.1": 7_000_000_000,
    "mistralai/Mistral-7B-v0.3": 7_000_000_000,
    "mistralai/Mistral-7B-Instruct-v0.1": 7_000_000_000,
    "mistralai/Mistral-7B-Instruct-v0.2": 7_000_000_000,
    "mistralai/Mistral-7B-Instruct-v0.3": 7_000_000_000,
    # Mixtral models
    "mistralai/Mixtral-8x7B-v0.1": 56_000_000_000,
    "mistralai/Mixtral-8x7B-Instruct-v0.1": 56_000_000_000,
    # Gemma models
    "google/gemma-2b": 2_510_000_000,
    "google/gemma-7b": 8_540_000_000,
    "google/gemma-2b-it": 2_510_000_000,
    "google/gemma-7b-it": 8_540_000_000,
    # Zephyr models (estimated size)
    "HuggingFaceH4/zephyr-7b-alpha": 7_000_000_000,
    "HuggingFaceH4/zephyr-7b-beta": 7_000_000_000,
    # Llama2 models
    "meta-llama/Llama-2-7b-hf": 7_000_000_000,
    "meta-llama/Llama-2-13b-hf": 13_000_000_000,
    "meta-llama/Llama-2-70b-hf": 70_000_000_000,
    "meta-llama/Llama-2-7b-chat-hf": 7_000_000_000,
    "meta-llama/Llama-2-13b-chat-hf": 13_000_000_000,
    "meta-llama/Llama-2-70b-chat-hf": 70_000_000_000,
    # Llama3 models (estimated sizes)
    "meta-llama/Meta-Llama-3-8B": 8_000_000_000,
    "meta-llama/Meta-Llama-3-8B-Instruct": 8_000_000_000,
    "meta-llama/Meta-Llama-3-70B": 70_000_000_000,
    "meta-llama/Meta-Llama-3-70B-Instruct": 70_000_000_000,
}

model2base_model = {
    # Qwen models
    "Qwen/Qwen1.5-0.5B": "qwen1.5",
    "Qwen/Qwen1.5-0.5B-Chat": "qwen1.5",
    "Qwen/Qwen1.5-1.8B": "qwen1.5",
    "Qwen/Qwen1.5-1.8B-Chat": "qwen1.5",
    "Qwen/Qwen1.5-4B": "qwen1.5",
    "Qwen/Qwen1.5-4B-Chat": "qwen1.5",
    "Qwen/Qwen1.5-7B": "qwen1.5",
    "Qwen/Qwen1.5-7B-Chat": "qwen1.5",
    "Qwen/Qwen1.5-14B": "qwen1.5",
    "Qwen/Qwen1.5-14B-Chat": "qwen1.5",
    "Qwen/Qwen1.5-32B": "qwen1.5",
    "Qwen/Qwen1.5-32B-Chat": "qwen1.5",
    "Qwen/Qwen1.5-72B": "qwen1.5",
    "Qwen/Qwen1.5-72B-Chat": "qwen1.5",
    "Qwen/Qwen2-0.5B": "qwen1.5",
    "Qwen/Qwen2-0.5B-Instruct": "qwen1.5",
    "Qwen/Qwen2-1.5B": "qwen1.5",
    "Qwen/Qwen2-1.5B-Instruct": "qwen1.5",
    "Qwen/Qwen2-7B": "qwen1.5",
    "Qwen/Qwen2-7B-Instruct": "qwen1.5",
    "Qwen/Qwen2-72B": "qwen1.5",
    "Qwen/Qwen2-72B-Instruct": "qwen1.5",
    "Qwen/Qwen2.5-3B":"qwen2.5",
    # Yi models
    "01-ai/Yi-6B": "yi",
    "01-ai/Yi-6B-Chat": "yi",
    "01-ai/Yi-9B": "yi",
    "01-ai/Yi-9B-Chat": "yi",
    "01-ai/Yi-34B": "yi",
    "01-ai/Yi-34B-Chat": "yi",
    "01-ai/Yi-1.5-6B": "yi",
    "01-ai/Yi-1.5-6B-Chat": "yi",
    "01-ai/Yi-1.5-9B": "yi",
    "01-ai/Yi-1.5-9B-Chat": "yi",
    "01-ai/Yi-1.5-34B": "yi",
    "01-ai/Yi-1.5-34B-Chat": "yi",
    # Mistral models
    "mistralai/Mistral-7B-v0.1": "mistral",
    "mistralai/Mistral-7B-v0.3": "mistral",
    "mistralai/Mistral-7B-Instruct-v0.1": "mistral",
    "mistralai/Mistral-7B-Instruct-v0.2": "mistral",
    "mistralai/Mistral-7B-Instruct-v0.3": "mistral",
    # Mixtral models
    "mistralai/Mixtral-8x7B-v0.1": "mixtral",
    "mistralai/Mixtral-8x7B-Instruct-v0.1": "mixtral",
    # Gemma models
    "google/gemma-2b": "gemma",
    "google/gemma-7b": "gemma",
    "google/gemma-2b-it": "gemma",
    "google/gemma-7b-it": "gemma",
    # Zephyr models
    "HuggingFaceH4/zephyr-7b-alpha": "zephyr",
    "HuggingFaceH4/zephyr-7b-beta": "zephyr",
    # Llama2 models
    "meta-llama/Llama-2-7b-hf": "llama2",
    "meta-llama/Llama-2-13b-hf": "llama2",
    "meta-llama/Llama-2-70b-hf": "llama2",
    "meta-llama/Llama-2-7b-chat-hf": "llama2",
    "meta-llama/Llama-2-13b-chat-hf": "llama2",
    "meta-llama/Llama-2-70b-chat-hf": "llama2",
    # Llama3 models
    "meta-llama/Meta-Llama-3-8B": "llama3",
    "meta-llama/Meta-Llama-3-8B-Instruct": "llama3",
    "meta-llama/Meta-Llama-3-70B": "llama3",
    "meta-llama/Meta-Llama-3-70B-Instruct": "llama3",
}
