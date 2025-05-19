multi_choice_prompt = {
    "normal": "以下是一道农学单项选择题，不需要做任何分析和解释，直接输出答案。\n\n问题：{question}\n选项：{options_str}\n答案：",
    "cot": "以下是一道农学单项选择题，请一步一步地思考，并在最后给出答案。\n\n问题：{question}\n选项：{options_str}\n答案：",
    "few_shot": {
        "instruction": "以下是几道农学单项选择题的示例，根据每道题直接输出答案，无需做任何分析和解释。",
        "example_template": "示例{i}\n问题：{question}\n\n选项：{options_str}\n答案：",
        "example_response": "答案：{answer}",
        "final_template": "现在，请根据以下题目输出答案：\n\n问题：{question}\n选项：{options_str}\n答案："
    }
}

dataset_examples = {
    "Disease-P": [
        {
            "id": "Disease_Per_546",
            "image_path": "Dz_1_25.JPG",
            "question": "图片中出现的是哪种作物？",
            "options": {
                "A": "大豆",
                "B": "玉米",
                "C": "水稻",
                "D": "小麦"
            },
            "answer": "D"
        },
            {
            "id": "Disease_Per_638",
            "image_path": "Dz_25_16.jpg",
            "question": "这张图片中的作物是什么？",
            "options": {
                "A": "玉米",
                "B": "小麦",
                "C": "大豆",
                "D": "水稻"
            },
            "answer": "D"
        },
        {
            "id": "Disease_Per_1035",
            "image_path": "Dz_59_34.jpg",
            "question": "图片中出现的是哪种作物？",
            "options": {
                "A": "大豆",
                "B": "小麦",
                "C": "玉米",
                "D": "水稻"
            },
            "answer": "C"
        },
        {
            "id": "Disease_Per_76",
            "image_path": "Dz_143_17.jpg",
            "question": "这片叶子属于哪种果树？",
            "options": {
                "A": "樱桃树",
                "B": "桃树",
                "C": "苹果树",
                "D": "梨树"
            },
            "answer": "C"
        }
    ],
    "Disease-M": [
        {
            "id": "Disease_MPC_546",
            "image_path": "Dz_1_25.JPG",
            "question": "这片小麦叶子可能感染了哪种疾病？",
            "options": {
                "A": "小麦白粉病",
                "B": "水稻稻瘟病",
                "C": "小麦条锈病",
                "D": "玉米黑粉病"
            },
            "answer": "C"
        },
        {
            "id": "Disease_MPC_638",
            "image_path": "Dz_25_16.jpg",
            "question": "请判断图片中水稻所患的病害是什么？",
            "options": {
                "A": "水稻黑粉病",
                "B": "水稻纹枯病",
                "C": "稻瘟病",
                "D": "小麦锈病"
            },
            "answer": "C"
        },
        {
            "id": "Disease_MPC_1035",
            "image_path": "Dz_59_34.jpg",
            "question": "图片中的玉米感染了哪种疾病？",
            "options": {
                "A": "玉米锈病",
                "B": "玉米大斑病",
                "C": "番茄晚疫病",
                "D": "水稻稻瘟病"
            },
            "answer": "B"
        },
        {
            "id": "Disease_MPC_76",
            "image_path": "Dz_143_17.jpg",
            "question": "这片苹果叶子上可能出现了什么病害？",
            "options": {
                "A": "苹果黑星病",
                "B": "苹果锈病",
                "C": "小麦锈病",
                "D": "水稻白叶枯病"
            },
            "answer": "A"
        }
    ],
    "Disease-K": [
        {
            "id": "Disease_MK_1256",
            "question": "小麦条锈病中的黄色孢子堆通常具有怎样的排列特征？",
            "options": {
                "A": "随机",
                "B": "零星",
                "C": "成行",
                "D": "集中"
            },
            "answer": "C"
        },
        {
            "id": "Disease_MK_1483",
            "question": "稻瘟病的病原孢子梗的尺寸特征是什么？",
            "options": {
                "A": "细长2μm",
                "B": "厚短6μm",
                "C": "长4μm",
                "D": "短3μm"
            },
            "answer": "C"
        },
        {
            "id": "Disease_MK_2440",
            "question": "玉米大斑病在玉米植物上的传播主要通过什么方式进行？",
            "options": {
                "A": "风雨传播",
                "B": "土壤传播",
                "C": "种子传播",
                "D": "根部传播"
            },
            "answer": "A"
        },
        {
            "id": "Disease_MK_182",
            "question": "苹果黑星病的病原形态特征与下列哪项最为一致？",
            "options": {
                "A": "倒梨形",
                "B": "圆柱形",
                "C": "球形",
                "D": "棒状"
            },
            "answer": "A"
        }
    ],
    "Disease-P-M": [
        {
            "id": "Disease_Per_MPC_546",
            "image_path": "Dz_1_25.JPG",
            "question": "这片叶子可能感染了哪种疾病？",
            "options": {
                "A": "小麦白粉病",
                "B": "水稻稻瘟病",
                "C": "小麦条锈病",
                "D": "玉米黑粉病"
            },
            "answer": "C"
        },
        {
            "id": "Disease_Per_MPC_638",
            "image_path": "Dz_25_16.jpg",
            "question": "请判断图片中作物所患的病害是什么？",
            "options": {
                "A": "水稻黑粉病",
                "B": "水稻纹枯病",
                "C": "稻瘟病",
                "D": "小麦锈病"
            },
            "answer": "C"
        },
        {
            "id": "Disease_Per_MPC_1035",
            "image_path": "Dz_59_34.jpg",
            "question": "图片中的作物感染了哪种疾病？",
            "options": {
                "A": "玉米锈病",
                "B": "玉米大斑病",
                "C": "番茄晚疫病",
                "D": "水稻稻瘟病"
            },
            "answer": "B"
        },
        {
            "id": "Disease_Per_MPC_76",
            "image_path": "Dz_143_17.jpg",
            "question": "这片叶子上可能出现了什么病害？",
            "options": {
                "A": "苹果黑星病",
                "B": "苹果锈病",
                "C": "小麦锈病",
                "D": "水稻白叶枯病"
            },
            "answer": "A"
        }
    ],
    "Disease-M-K": [
        {
            "id": "Disease_MPC_MK_1256",
            "image_path": "Dz_1_25.JPG",
            "question": "图片中小麦叶片上的黄色孢子堆通常会有哪些排列特征？",
            "options": {
                "A": "随机",
                "B": "零星",
                "C": "成行",
                "D": "集中"
            },
            "answer": "C"
        },
        {
            "id": "Disease_MPC_MK_1483",
            "image_path": "Dz_25_16.jpg",
            "question": "图片中水稻所相关的病原孢子梗的尺寸特征是什么？",
            "options": {
                "A": "细长2μm",
                "B": "厚短6μm",
                "C": "长4μm",
                "D": "短3μm"
            },
            "answer": "C"
        },
        {
            "id": "Disease_MPC_MK_2440",
            "image_path": "Dz_59_34.jpg",
            "question": "图片中玉米植株的感染途径主要是通过什么方式传播？",
            "options": {
                "A": "风雨传播",
                "B": "土壤传播",
                "C": "种子传播",
                "D": "根部传播"
            },
            "answer": "A"
        },
        {
            "id": "Disease_MPC_MK_182",
            "image_path": "Dz_143_17.jpg",
            "question": "图中苹果的病原形态特征与下列哪项最为一致？",
            "options": {
                "A": "倒梨形",
                "B": "圆柱形",
                "C": "球形",
                "D": "棒状"
            },
            "answer": "A"
        }
    ],
    "Disease-P-M-K": [
        {
            "id": "Disease_Per_MPC_MK_1256",
            "image_path": "Dz_1_25.JPG",
            "question": "图片中叶片上的黄色孢子堆通常会有怎样的排列特征？",
            "options": {
                "A": "随机",
                "B": "零星",
                "C": "成行",
                "D": "集中"
            },
            "answer": "C"
        },
        {
            "id": "Disease_Per_MPC_MK_1483",
            "image_path": "Dz_25_16.jpg",
            "question": "图片中作物所相关的病原孢子梗的尺寸特征是什么？",
            "options": {
                "A": "细长2μm",
                "B": "厚短6μm",
                "C": "长4μm",
                "D": "短3μm"
            },
            "answer": "C"
        },
        {
            "id": "Disease_Per_MPC_MK_2440",
            "image_path": "Dz_59_34.jpg",
            "question": "图片中植物的感染途径主要是通过什么方式传播？",
            "options": {
                "A": "风雨传播",
                "B": "土壤传播",
                "C": "种子传播",
                "D": "根部传播"
            },
            "answer": "A"
        },
        {
            "id": "Disease_Per_MPC_MK_182",
            "image_path": "Dz_143_17.jpg",
            "question": "图中植物的病原形态特征与下列哪项最为一致？",
            "options": {
                "A": "倒梨形",
                "B": "圆柱形",
                "C": "球形",
                "D": "棒状"
            },
            "answer": "A"
        }
    ],
    "Pest-P": [
        {
            "id": "Pest_Per_2",
            "image_path": "Dz_100_10.jpg",
            "question": "图片中出现的是以下哪种害虫？",
            "options": {
                "A": "绿盲蝽",
                "B": "棉铃虫",
                "C": "稻纵卷叶螟",
                "D": "刺蛾科"
            },
            "answer": "D"
        },
        {
            "id": "Pest_Per_712",
            "image_path": "Dz_12_35.jpg",
            "question": "图片中显示的是哪种害虫？",
            "options": {
                "A": "蝗虫",
                "B": "红蜘蛛",
                "C": "麦二叉蚜",
                "D": "草地贪夜蛾"
            },
            "answer": "C"
        },
        {
            "id": "Pest_Per_1838",
            "image_path": "Dz_60_5.jpg",
            "question": "图片中出现的是以下哪种害虫？",
            "options": {
                "A": "瓢虫",
                "B": "蚊子",
                "C": "蚜虫",
                "D": "蝽虫"
            },
            "answer": "C"
        },
        {
            "id": "Pest_Per_2257",
            "image_path": "Dz_83_10.jpg",
            "question": "图片中出现的是以下哪种害虫？",
            "options": {
                "A": "牧草盲蝽",
                "B": "蚜虫",
                "C": "稻飞虱",
                "D": "斜纹夜蛾"
            },
            "answer": "A"
        }
    ],
    "Pest-K": [
        {
            "id": "Pest_MK_2",
            "question": "触碰刺蛾科幼虫通常会对皮肤产生什么影响？",
            "options": {
                "A": "感觉凉爽",
                "B": "皮肤红肿",
                "C": "没有感觉",
                "D": "变得清晰"
            },
            "answer": "B"
        },
        {
            "id": "Pest_MK_1604",
            "question": "麦二叉蚜更偏好生活在怎样的环境中？",
            "options": {
                "A": "阳光充足",
                "B": "潮湿多雨",
                "C": "干燥",
                "D": "阴冷"
            },
            "answer": "C"
        },
        {
            "id": "Pest_MK_4282",
            "question": "负责吸收太阳能的色素集中分布于蚜虫身体的哪个部位？",
            "options": {
                "A": "触角末端",
                "B": "角质层深处",
                "C": "翅膀表面",
                "D": "腹部下方"
            },
            "answer": "B"
        },
        {
            "id": "Pest_MK_5259",
            "question": "根据牧草盲蝽的习性推测，它们的卵阶段大约需要多少天才能孵化？",
            "options": {
                "A": "10天",
                "B": "20天",
                "C": "30天",
                "D": "40天"
            },
            "answer": "A"
        },
    ],
    "Pest-P-K": [
        {
            "id": "Pest_Per_MK_2",
            "image_path": "Dz_100_10.jpg",
            "question": "触碰图中所示幼虫通常会对皮肤产生什么影响？",
            "options": {
                "A": "感觉凉爽",
                "B": "皮肤红肿",
                "C": "没有感觉",
                "D": "变得清晰"
            },
            "answer": "B"
        },
        {
            "id": "Pest_Per_MK_1604",
            "image_path": "Dz_12_35.jpg",
            "question": "图中害虫更偏好生活在怎样的环境中？",
            "options": {
                "A": "阳光充足",
                "B": "潮湿多雨",
                "C": "干燥",
                "D": "阴冷"
            },
            "answer": "C"
        },
        {
            "id": "Pest_Per_MK_4282",
            "image_path": "Dz_60_5.jpg",
            "question": "图中显示的害虫中，负责吸收太阳能的色素集中分布于身体的哪个部位？",
            "options": {
                "A": "触角末端",
                "B": "角质层深处",
                "C": "翅膀表面",
                "D": "腹部下方"
            },
            "answer": "B"
        },
        {
            "id": "Pest_Per_MK_5259",
            "image_path": "Dz_83_10.jpg",
            "question": "观察图中害虫，根据害虫的习性推测，它们的卵阶段大约需要多少天才能孵化？",
            "options": {
                "A": "10天",
                "B": "20天",
                "C": "30天",
                "D": "40天"
            },
            "answer": "A"
        }
    ]
}