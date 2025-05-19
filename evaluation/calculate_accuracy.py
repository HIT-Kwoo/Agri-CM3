import os
import json
import re
import argparse
import pandas as pd

def match_choice(options: dict, response: str) -> str:
    if not response:
        return "None"
        
    for v in options.values():
        response = response.replace(v, "")
    res = re.findall(r'[A-D]', response)
    
    return res[-1] if res else "None"

def calculate_accuracy(result_folder: str, out_file: str):
    dataset_names = ["Disease-P", "Disease-M", "Disease-K", "Disease-P-M", "Disease-M-K", "Disease-P-M-K", "Pest-P", "Pest-K", "Pest-P-K"]
    
    results = []
    
    for dataset_name in dataset_names:
        dataset_path = os.path.join(result_folder, dataset_name)
        for prompt in os.listdir(dataset_path):
            prompt_path = os.path.join(dataset_path, prompt)
            if os.path.isdir(prompt_path):
                for file_name in os.listdir(prompt_path):
                    if file_name.endswith(".json"):
                        model_name, *_ = file_name.split("_")
                        prompt_type = prompt
                        correct = 0
                        questions = 0
                        
                        file_path = os.path.join(prompt_path, file_name)
                        with open(file_path, "r", encoding="utf-8") as f:
                            data = json.load(f)
                        
                        for item in data:
                            questions += 1
                            if match_choice(item["options"], item["response"]) == item["answer"]:
                                correct += 1
                        
                        accuracy = correct / questions if questions > 0 else 0
                        results.append([model_name, prompt_type, dataset_name, accuracy])
    
    df = pd.DataFrame(results, columns=["Model", "Prompt", "DataType", "Accuracy"])
    
    total_results = df.groupby(["Model", "Prompt"], as_index=False).agg({"Accuracy": "mean"})
    total_results["DataType"] = "Overall"
    
    df = pd.concat([df, total_results], ignore_index=True)
    
    df_pivot = df.pivot_table(index=["Model", "Prompt"], columns="DataType", values="Accuracy").reset_index()
    
    columns_order = ["Model", "Prompt"] + dataset_names + ["Overall"]
    df_pivot = df_pivot.reindex(columns=columns_order)
    
    df_pivot.to_excel(out_file, index=False)
    
    print("Results saved to", out_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--result_folder", type=str, required=True, help="Folder containing the result JSON files")
    parser.add_argument("--out_file", type=str, required=True, help="Output Excel file path")
    
    args = parser.parse_args()
    
    calculate_accuracy(args.result_folder, args.out_file)