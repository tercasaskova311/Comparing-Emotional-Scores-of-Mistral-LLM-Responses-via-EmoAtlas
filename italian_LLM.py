#FAUNO

! pip3 install -i https://test.pypi.org/simple/ bitsandbytes
! pip3 install -q -U git+https://github.com/huggingface/accelerate.git

! pip3 install datasets==2.11.0 loralib sentencepiece git+https://github.com/huggingface/transformers.git gradio appdirs
! pip3 install -q -U git+https://github.com/huggingface/peft.git


#requirements--------------------
from typing import *
from transformers import LlamaTokenizer, LlamaForCausalLM, GenerationConfig
from peft import PeftModel
import torch
import transformers

#model setup-----------------------
tokenizer = LlamaTokenizer.from_pretrained("decapoda-research/llama-7b-hf")
model = LlamaForCausalLM.from_pretrained(
    "decapoda-research/llama-7b-hf",
    load_in_8bit=True,
    device_map="auto",
)
model = PeftModel.from_pretrained(model, "andreabac3/Fauno-Italian-LLM-7B")
model.eval()


# -- Generate JSON prompts with Fauno (fixed and updated) --

def generate_prompt(text: str, history: List[Tuple[str, str]], tokenizer, max_length=2048):
    system_prompt = {
        "role": "user",
        "content": (
            "I want to generate 200 prompts to use with an LLM. Each prompt should ask for someone's opinion "
            "and must appear in both English and Italian. The topic should vary (e.g., food, travel, ethics, daily life). "
            "Use this JSON format:\n\n"
            "{\n  \"prompts\": [\n    {\n      \"english\": \"What do you think about vegetarianism? "
            "Is it a healthy way to eat?\",\n      \"italian\": \"Cosa ne pensi del vegetarianismo? "
            "È un modo sano di mangiare?\"\n    },\n    {\n      \"english\": \"...\",\n      \"italian\": \"...\"\n    }\n"
            "// 198 more entries\n  ]\n}\n\nPlease generate 200 such pairs."
        )
    }

    # Combine the past history into a long string (backward)
    history_blocks = ["\n[|Human|] {}\n[|AI|] {}".format(user, bot) for user, bot in history]
    new_input = "\n[|Human|] {}\n[|AI|]".format(text)

    # Build up the full history from latest to oldest
    full_prompt = ""
    flag = False
    for turn in reversed(history_blocks + [new_input]):
        temp_prompt = full_prompt = turn + full_prompt
        tokenized = tokenizer(system_prompt["content"] + full_prompt, return_tensors="pt")
        if tokenized['input_ids'].size(-1) <= max_length:
            flag = True
        else:
            break

    if not flag:
        return False

    # Final full prompt
    final_prompt = system_prompt["content"] + full_prompt
    inputs = tokenizer(final_prompt, return_tensors="pt").to(model.device)

    return final_prompt, inputs

