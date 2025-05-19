# The script is used to test online model with normal prompt type on the validation dataset.
python scripts/test_mllm.py \
    --model_name "gpt-4o" \
    --temperature 1.0 \
    --max_tokens 1024 \
    --api_url "https://api.openai.com/v1/engines/gpt-4o/completions" \
    --api_key "your_api_key" \
    --prompt_type "normal" \
    --dataset_dir "data/valid" \
    --image_dir "data/images" \
    --output_dir "results/valid"

# The script is used to test local model with 1_shot prompt type on the test dataset.
vllm serve Qwen/Qwen2-VL-7B-Instruct --limit-mm-per-prompt image=5
python scripts/test_mllm.py \
    --model_name Qwen/Qwen2-VL-7B-Instruct \
    --temperature 1.0 \
    --max_tokens 1024 \
    --api_url "http://localhost:8000/v1" \
    --api_key "EMPTY" \
    --prompt_type "1_shot" \
    --dataset_dir "data/test" \
    --image_dir "data/images" \
    --output_dir "results/test"

# The script is used to calculate the accuracy of the model on the validation dataset.
python scripts/calculate_accuracy.py \
    --result_folder "results/valid" \
    --out_file "results/valid_accuracy.xlsx"

# The script is used to test online model with normal prompt type on the test dataset.
python scripts/calculate_accuracy.py \
    --result_folder "results/test" \
    --out_file "results/test_accuracy.xlsx"