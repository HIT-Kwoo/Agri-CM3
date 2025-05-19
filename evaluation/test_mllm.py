import os
import json
import time
import base64
import argparse
from tqdm import tqdm

from agent_openai import Agent_OpenAI
from prompts import multi_choice_prompt, dataset_examples

def get_output_path(args, dataset_name: str) -> str:
    output_dir = os.path.join(args.output_dir, dataset_name, args.prompt_type)
    os.makedirs(output_dir, exist_ok=True)
    
    model_name = args.model_name.split("/")[-1] if "/" in args.model_name else args.model_name
    f_name = f'{model_name}_prompt-{args.prompt_type}.json'
    return os.path.join(output_dir, f_name)

def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def format_options(options: dict) -> str:
    return "\n".join([f"{k}. {v}" for k, v in options.items() if v.strip()])

def get_no_shot_messages(item: dict, prompt_type: str, args) -> list:
    question = item["question"]
    options_str = format_options(item["options"])
    prompt_template = multi_choice_prompt[prompt_type]
    prompt = prompt_template.format(question=question, options_str=options_str)

    content = [{"type": "text", "text": prompt}]
    if "image_path" in item:
        image_path = os.path.join(args.image_dir, item["image_path"])
        content.append({"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encode_image(image_path)}"}})
    
    messages = [{"role": "user", "content": content}]
    return messages

def get_few_shot_messages(item: dict, prompt_type: str, dataset_name: str, args) -> list:
    num_shots = int(prompt_type.split("_")[0])
    examples = dataset_examples[dataset_name][:num_shots]
    prompt_template = multi_choice_prompt["few_shot"]
    
    messages = [{"role": "user", "content": [{"type": "text", "text": prompt_template["instruction"]}]}]
    
    for i, example in enumerate(examples, start=1):
        options_str = format_options(example["options"])
        content = [{"type": "text", "text": prompt_template["example_template"].format(i=i, question=example["question"], options_str=options_str)}]
        
        if "image_path" in example:
            image_path = os.path.join(args.image_dir, example["image_path"])
            content.append({"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encode_image(image_path)}"}})
        
        content.append({"type": "text", "text": prompt_template["example_response"].format(answer=example['answer'])})
        messages.append({"role": "user", "content": content})
    
    options_str = format_options(item["options"])
    content = [{"type": "text", "text": prompt_template["final_template"].format(question=item["question"], options_str=options_str)}]
    
    if "image_path" in item:
        image_path = os.path.join(args.image_dir, item["image_path"])
        content.append({"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encode_image(image_path)}"}})
    
    messages.append({"role": "user", "content": content})
    
    return messages

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", type=str)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max_tokens", type=int, default=1024)
    parser.add_argument("--api_url", type=str)
    parser.add_argument("--api_key", type=str)
    parser.add_argument("--prompt_type", type=str, default="normal", choices=["normal", "cot", "1_shot", "2_shot", "3_shot", "4_shot"])
    parser.add_argument("--dataset_dir", type=str, default="./data/test")
    parser.add_argument("--image_dir", type=str, default="./data/images")
    parser.add_argument("--output_dir", type=str, default="./results/test")

    args = parser.parse_args()
    print(args)
    
    dataset_names = ["Disease-P", "Disease-M", "Disease-K", "Disease-P-M", "Disease-M-K", "Disease-P-M-K", "Pest-P", "Pest-K", "Pest-P-K"]
    
    for dataset_name in dataset_names:
        data_path = os.path.join(args.dataset_dir, f"{dataset_name}.json")
    
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # demo
        data = data[:10]

        output_path = get_output_path(args, dataset_name)
        
        if os.path.exists(output_path):
            with open(output_path, "r", encoding="utf-8") as fr_infer:
                had_inference_data = json.load(fr_infer)
        else:
            had_inference_data = []

        had_inference_ids = {item["id"] for item in had_inference_data}
        
        agent = Agent_OpenAI(args)
        
        for item in tqdm(data):
            if item["id"] in had_inference_ids:
                continue
            
            prompt_type = args.prompt_type
            
            if prompt_type in ["normal", "cot"]:
                messages = get_no_shot_messages(item, prompt_type, args)
            else:
                messages = get_few_shot_messages(item, prompt_type, dataset_name, args)

            response = agent.forward(messages)
            item["response"] = response
            
            had_inference_data.append(item)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(had_inference_data, f, ensure_ascii=False, indent=4)

            if args.prompt_type == "normal":
                time.sleep(0.2)