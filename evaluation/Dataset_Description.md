# Agri-CM<sup>3</sup> Description

**Agri-CM<sup>3</sup>: A Chinese Massive Multi-modal, Multi-level Benchmark for Agricultural Understanding and Reasoning**

## 1. Introduction

The Agri-CM<sup>3</sup> project aims to provide a comprehensive framework to assess and enhance AI models' understanding and reasoning capabilities concerning diseases and pests in agriculture. By integrating textual information with image data, Agri-M3 not only tests models' ability to handle single-type information but also explores their performance on multimodal data. This benchmark particularly emphasizes the identification of crops, diseases, or pests and their characteristic analysis, thus comprehensively evaluating the model's potential in practical applications. Based on professional background knowledge and real cases, Agri-CM<sup>3</sup> designs a series of complex data generation processes, ensuring the quality and diversity of questions, providing valuable research resources for researchers. 

## 2. Dataset File Description 

The Agri-CM<sup>3</sup> dataset includes various types of questions categorized across different dimensions, covering knowledge levels from basic to advanced. Here are detailed descriptions of each file in the dataset: 

- Disease-P.json: Focuses on disease recognition specific to certain crops, containing questions requiring models to identify specific crops and diagnose their diseases. 
- Disease-M.json: Involves diagnosing diseases for specific crops, suitable for assessing models' comprehension abilities at mixed perception levels. 
- Disease-K.json: Contains questions about the knowledge dimension of specific diseases, asking users to accurately judge relevant disease information. 
- Disease-M-K.json: Offers questions ideal for comprehensive evaluation of specific crops, helping test models' performance in multi-step reasoning tasks. 
- Disease-P-M.json: Questions in this file require models not only to recognize crops but also understand related disease diagnostic methods. 
- Disease-P-M-K.json: As one of the most complex disease recognition tasks, this file covers crop identification, disease diagnosis, and corresponding management measures, crucial for testing models' all-around reasoning capabilities. 
- Pest-P.json: Requires models to accurately identify pests. 
- Pest-K.json: Focuses on foundational knowledge about pests, asking users to accurately judge pest-related information. 
- Pest-P-K.json: Integrates pest identification with management strategies, aiming to evaluate models' comprehensive abilities in handling complex pest issues.

## 3. Data Field Description

Here are detailed explanations of fields within the dataset: 

- id: Unique identifier for data items. 
- crop_name: Name of the agricultural crop. 
- disease_name: Name of the disease or pest. 
- question: The problem description provided to the model. 
- options: Available answer choices. 
- answer: The correct option among answers. 
- options_analysis: Detailed explanations for each option, aiding understanding of why an option is correct or incorrect. 

## 4. Usage Instructions 

### 4.1 Installation Steps 

Clone the repository.

Install dependency packages: 

```bash
pip install -r requirements.txt 
```

Download images and unzip them into the data folder. 

### 4.2 Testing Models

You can test both online and local models and generate result files. 

Testing Online Models Use normal prompt type to test online models on the validation dataset:

```bash
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
```

Testing Local Models Install vLLM to provide API services for local models. Taking Qwen/Qwen2-VL-7B-Instruct as an example, run the following command to start the service: 

```bash
vllm serve Qwen/Qwen2-VL-7B-Instruct --limit-mm-per-prompt image=5
```

Use 1_shot prompt type to test local models on the test dataset: 

```bash
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
```

### 4.3 Calculating Accuracy
Calculate accuracy on the validation dataset:

```bash
python scripts/calculate_accuracy.py \
    --result_folder "results/valid" \
    --out_file "results/valid_accuracy.xlsx"
```

Calculate accuracy on the test dataset:

```bash
python scripts/calculate_accuracy.py \
    --result_folder "results/test" \
    --out_file "results/test_accuracy.xlsx"
```

<!-- ## 5. Application Process

For researchers and institutions wishing to participate in the Agri-M3 project and utilize its resources, please follow the formal application process outlined below:

1. **Prepare Required Materials**: Applicants should prepare the following documents:
   - A copy of the identity document of applicants with mid-to-senior professional titles from universities, research institutes, or enterprises.
   - A scanned copy of the signed cooperation agreement, ensuring that all necessary information is complete and accurate.
2. **Submit the Application**: Send all the prepared materials to the designated email address: [jiangjingchi@hit.edu.cn](mailto:jiangjingchi@hit.edu.cn). Please indicate "Agri-M3 Project Application - [Your Name or Institution's Name]" in the subject line of the email for quick identification and processing of your application.

Please note that only applications providing complete materials as required will be considered. Once your application is received, relevant staff will review it and contact you within a certain period to confirm the next steps or provide further information requirements. Thank you for your interest in and support of the Agri-M3 project! -->