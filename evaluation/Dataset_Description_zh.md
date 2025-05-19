# Agri-CM<sup>3</sup> 说明

**Agri-CM<sup>3</sup>：A Chinese Massive Multi-modal, Multi-level Benchmark for Agricultural Understanding and Reasoning**

## 1. 简介

Agri-CM<sup>3</sup>项目旨在提供一个全面的框架，以评估和增强大语言模型在农业领域中对病害和虫害的理解与推理能力。通过结合文本信息和图像数据，Agri-CM<sup>3</sup>不仅测试了模型处理单一类型信息的能力，还探索了其在多模态数据上的表现。该基准特别强调了作物、病害或虫害的识别及其特征分析，从而全面考察模型在实际应用中的潜力。基于专业背景知识和实际案例，Agri-CM<sup>3</sup>设计了一系列复杂的数据生成流程，确保了问题的质量和多样性，为研究者提供了宝贵的研究资源。

## 2. 数据集文件说明

Agri-CM<sup>3</sup>数据集包括多种类型的题目，这些题目按照不同的维度进行分类，涵盖了从基础到高级的知识层次。以下是数据集中各文件的具体描述：

- Disease-P.json：专注于特定作物的病害识别，此文件包含了需要模型识别具体作物并判断其病害的问题。
- Disease-M.json：此文件涉及针对特定作物进行病害诊断的考察，适用于评估模型在混合感知层次上的理解能力。
- Disease-K.json：此文件包含关于特定病害的知识维度的问题，要求用户准确判断病害的相关信息。
- Disease-M-K.json：此文件提供的问题是针对特定作物进行综合评估的理想选择，帮助检验模型在多步骤推理任务中的表现。
- Disease-P-M.json：此文件中的问题要求模型不仅要识别作物，还需了解相关的病害诊断方法。
- Disease-P-M-K.json：作为最复杂的病害识别任务之一，此文件中的问题覆盖了作物识别、病害诊断以及相应的管理措施，是测试模型全方位推理能力的关键。
- Pest-P.json：此文件中的问题要求模型能够准确地辨别害虫。
- Pest-K.json：此文件关注于害虫的基础知识，要求用户准确判断虫害的相关信息。
- Pest-P-K.json：整合了害虫识别与管理策略，此文件中的问题旨在评估模型在处理复杂害虫问题时的综合能力。

## 3. 数据字段说明

以下是对数据集中字段的详细说明：

- **id**: 数据项的唯一标识符。
- **crop_name**: 农作物名称。
- **disease_name**: 病害或虫害的名称。
- **question**: 提供给模型的问题描述。
- **options**: 可选答案。
- **answer**: 正确的答案选项。
- **options_analysis**: 对每个选项的详细解释，帮助理解为什么某个选项是正确的或不正确的。

## 4. 使用方法

### 4.1 安装步骤

1. **克隆仓库** 

2. **安装依赖包**：

   

   ```
   pip install -r requirements.txt
   ```

3. **下载数据集并解压缩到`data`文件夹**。

### 4.2 测试模型

你可以测试在线和本地模型，并生成结果文件。

#### 测试在线模型

使用正常提示类型在验证数据集上测试在线模型：

```
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

#### 测试本地模型

安装 vLLM 来为本地模型提供 API 服务。以 Qwen/Qwen2-VL-7B-Instruct 为例，运行以下命令启动服务：

```
vllm serve Qwen/Qwen2-VL-7B-Instruct --limit-mm-per-prompt image=5
```

使用 1_shot 提示类型在测试数据集上测试本地模型：

```
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

### 4.3 计算准确率

在验证数据集上计算准确率：

```
python scripts/calculate_accuracy.py \
    --result_folder "results/valid" \
    --out_file "results/valid_accuracy.xlsx"
```

在测试数据集上计算准确率：

```
python scripts/calculate_accuracy.py \
    --result_folder "results/test" \
    --out_file "results/test_accuracy.xlsx"
```

<!-- ## 5. 申请流程

对于希望参与Agri-M3项目并使用其资源的研究人员或机构，请遵循以下书面申请流程：

1. **准备所需材料**：申请人需准备如下材料：
   - 高校、科研院所、企事业单位具有中、高级职称申请人员的身份证明复印件。
   - 申请人员签署的合作协议扫描件，确保所有必要信息完整且准确无误。
2. **提交申请**：将上述准备的所有材料发送至指定邮箱地址：[jiangjingchi@hit.edu.cn](mailto:jiangjingchi@hit.edu.cn)。请在邮件主题栏注明“Agri-M3项目申请-[您的姓名或单位名称]”，以便快速识别和处理您的申请。

请注意，只有按照上述要求提供完整申请材料的申请才会被考虑。一旦收到您的申请，相关工作人员将会进行审核，并在一定时间内与您联系以确认后续步骤或提供进一步的信息需求。感谢您对Agri-M3项目的关注和支持！ -->
