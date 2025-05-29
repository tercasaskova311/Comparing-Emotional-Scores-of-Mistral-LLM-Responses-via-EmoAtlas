from typing import *
from transformers import LlamaTokenizer, LlamaForCausalLM, GenerationConfig
from peft import PeftModel
import torch
import transformers


def generate_prompt(text: str, tokenizer, max_length=2048):
    system_prompt = "You are Fauno, a helpful AI assistant.\n\n"
    full_prompt = system_prompt + text + "\nFauno:"

    inputs = tokenizer(full_prompt, return_tensors="pt")
    if inputs['input_ids'].size(-1) > max_length:
        print("Input too long!")
        return False

    return full_prompt, inputs.to(model.device)


import json

# Load prompts from file
with open('prompts.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

results = []

for prompt_pair in data['prompts']:
    # Combine English + Italian prompt text simply
    prompt_text = f"English: {prompt_pair['english']}\nItalian: {prompt_pair['italian']}"

    generated = generate_prompt(prompt_text, tokenizer)
    if not generated:
        continue

    full_prompt, inputs = generated

    # Generate response (simple settings)
    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=128,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            eos_token_id=tokenizer.eos_token_id,
        )

    # Decode just the generated part
    decoded = tokenizer.decode(output_ids[0][inputs['input_ids'].size(-1):], skip_special_tokens=True)

    results.append({
        "prompt": prompt_pair,
        "response": decoded.strip()
    })

# Save results
with open('fauno_responses.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
