<div align="center">

# Agri-CM<sup>3</sup>: A Chinese Massive Multi-modal, Multi-level Benchmark for Agricultural Understanding and Reasoning

</div>

This is the repository containing evaluation datas, instructions and demonstrations with ***ACL 2025*** paper _**Agri-CM<sup>3</sup>: A Chinese Massive Multi-modal, Multi-level Benchmark for Agricultural Understanding and Reasoning**_ ([Wang et al., 2025]())

## Agri-CM<sup>3</sup> Benchmark

### Design Principal
Existing benchmarks often evaluate complex reasoning tasks as a whole, especially for tasks involving multiple reasoning steps, such as agricultural knowledge reasoning. This approach fails to accurately identify model strengths and weaknesses at each reasoning stage, leading to a lack of clear guidance for future model improvements.

To address this limitation, we propose \datasetname{}, which aims to comprehensively assess the complex reasoning capabilities of models in agricultural pest and disease management through a multi-level evaluation framework. We decompose the complex reasoning task into three key sub-tasks:

1. Perception (P): The ability to identify crops and pests.
2. Mixed Perception-Cognition Reasoning (M): The ability to identify crop symptoms and reason diseases.
3. Knowledge Application (K): The ability to integrate and apply agricultural knowledge.

These key abilities are then combined into three levels based on task-specific needs:  

- Level 1: Evaluates model performance on a single sub-reasoning task.  
- Level 2: Assesses the model’s ability to perform a combination of two sub-reasoning tasks.  
- Level 3: Evaluates the model’s performance across the full reasoning chain.

Through this layered design, \datasetname{} provides a comprehensive evaluation of a model’s capabilities at different reasoning stages, offering detailed feedback on performance at each level. The overall data collection and generation process is illustrated in Figure 1.

### Construction Process

![Figure 1. An overview of the benchmark construction process.](assets/construction_process.png) 


### Datasets Statistics
![](assets/dataset_sunburst.png)


## Performance

![](assets/results.jpg)



<!-- ## Citation
If you find our work helpful, you can cite this paper as:

```bibtex
@misc{chu2023timebench,
      title={TimeBench: A Comprehensive Evaluation of Temporal Reasoning Abilities in Large Language Models}, 
      author={Zheng Chu and Jingchang Chen and Qianglong Chen and Weijiang Yu and Haotian Wang and Ming Liu and Bing Qin},
      year={2023},
      eprint={2311.17667},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2311.17667}
}
``` -->