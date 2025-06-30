<div align="center">
<img src="img/banner.png" alt="LLM Course">
  <p align="center">
    𝕏 <a href="https://twitter.com/maximelabonne">在 𝕏 上关注我</a> • 
    🤗 <a href="https://huggingface.co/mlabonne">Hugging Face</a> • 
    💻 <a href="https://mlabonne.github.io/blog">博客</a> • 
    📙 <a href="https://packt.link/a/9781836200079">LLM 工程师手册</a>
  </p>
</div>
<br/>

<a href="https://a.co/d/a2M67rE"><img align="right" width="25%" src="https://i.imgur.com/7iNjEq2.png" alt="LLM 工程师手册封面"/></a>LLM 课程分为三个部分：

1. 🧩 **LLM 基础** (可选)，涵盖了关于数学、Python 和神经网络的基础知识。
2. 🧑‍🔬 **LLM 科学家** 专注于使用最新技术构建最好的 LLM。
3. 👷 **LLM 工程师** 专注于创建基于 LLM 的应用程序并进行部署。

> [!NOTE]
> 基于本课程，我与 Paul Iuzstin 合著了 [LLM 工程师手册](https://packt.link/a/9781836200079)。这是一本内容详尽的实践性书籍，涵盖了从设计到部署的端到端 LLM 应用。LLM 课程将永远免费，但欢迎您通过购买本书来支持我的工作。

为了提供本课程的互动版本，我创建了一个 LLM 助手，它可以在 [**HuggingChat**](https://hf.co/chat/assistant/66029d2e5f4a884f7aabc9d1) 或 [**ChatGPT**](https://chat.openai.com/g/g-yviLuLqvI-llm-course) 上以个性化的方式回答问题并测试您的知识。

## 📝 Notebook

我编写的关于 LLM 的 Notebook 和文章列表。

### 工具

| Notebook | 描述 | Notebook |
|----------|-------------|----------|
| 🧐 [LLM AutoEval](https://github.com/mlabonne/llm-autoeval) | 使用 RunPod 自动评估您的 LLM | <a href="https://colab.research.google.com/drive/1Igs3WZuXAIv9X0vwqiE90QlEPys8e8Oa?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| 🥱 LazyMergekit | 使用 MergeKit 一键轻松合并模型。 | <a href="https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| 🦎 LazyAxolotl | 使用 Axolotl 一键在云端微调模型。 | <a href="https://colab.research.google.com/drive/1TsDKNo2riwVmU55gjuBgB1AXVtRRfRHW?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| ⚡ AutoQuant | 一键将 LLM 量化为 GGUF、GPTQ、EXL2、AWQ 和 HQQ 格式。 | <a href="https://colab.research.google.com/drive/1b6nqC7UZVt8bx4MksX7s656GXPM-eWw4?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| 🌳 Model Family Tree | 可视化合并模型的家族树。 | <a href="https://colab.research.google.com/drive/1s2eQlolcI1VGgDhqWIANfkfKvcKrMyNr?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| 🚀 ZeroSpace | 使用免费的 ZeroGPU 自动创建 Gradio 聊天界面。 | <a href="https://colab.research.google.com/drive/1LcVUW5wsJTO2NGmozjji5CkC--646LgC"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| ✂️ AutoAbliteration | 使用自定义数据集自动对模型进行 abliteration。 | <a href="https://colab.research.google.com/drive/1RmLv-pCMBBsQGXQIM8yF-OdCNyoylUR1?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| 🧼 AutoDedup | 使用 Rensa 库自动对数据集进行去重。 | <a href="https://colab.research.google.com/drive/1o1nzwXWAa8kdkEJljbJFW1VuI-3VZLUn?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |

### 微调

| Notebook | 描述 | 文章 | Notebook |
|---------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| 使用 Unsloth 微调 Llama 3.1 | 在 Google Colab 中进行超高效的监督微调。 | [文章](https://mlabonne.github.io/blog/posts/2024-07-29_Finetune_Llama31.html) | <a href="https://colab.research.google.com/drive/164cg_O7SV7G8kZr_JXqLd6VC7pd86-1Z?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| 使用 ORPO 微调 Llama 3 | 使用 ORPO 进行单阶段、更便宜、更快速的微调。 | [文章](https://mlabonne.github.io/blog/posts/2024-04-19_Fine_tune_Llama_3_with_ORPO.html) | <a href="https://colab.research.google.com/drive/1eHNWg9gnaXErdAa8_mcvjMupbSS6rDvi"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| 使用 DPO 微调 Mistral-7b | 使用 DPO 提升监督微调模型的性能。 | [文章](https://mlabonne.github.io/blog/posts/Fine_tune_Mistral_7b_with_DPO.html) | <a href="https://colab.research.google.com/drive/15iFBr1xWgztXvhrj5I9fBv20c7CFOPBE?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| 使用 QLoRA 微调 Mistral-7b | 在免费的 Google Colab 中使用 TRL 对 Mistral-7b 进行监督微调。 |  | <a href="https://colab.research.google.com/drive/1o_w0KastmEJNVwT5GoqMCciH-18ca5WS?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| 使用 Axolotl 微调 CodeLlama | 端到端的微调SOTA工具指南。 | [文章](https://mlabonne.github.io/blog/posts/A_Beginners_Guide_to_LLM_Finetuning.html) | <a href="https://colab.research.google.com/drive/1Xu0BrCB7IShwSWKVcfAfhehwjDrDMH5m?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| 使用 QLoRA 微调 Llama 2 | 在 Google Colab 中监督微调 Llama 2 的分步指南。 | [文章](https://mlabonne.github.io/blog/posts/Fine_Tune_Your_Own_Llama_2_Model_in_a_Colab_Notebook.html) | <a href="https://colab.research.google.com/drive/1PEQyJO1-f6j0S_XJ8DV50NkpzasXkrzd?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |

### 量化

| Notebook | 描述 | 文章 | Notebook |
|---------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| 量化简介 | 使用 8-bit 量化进行大语言模型优化。 | [文章](https://mlabonne.github.io/blog/posts/Introduction_to_Weight_Quantization.html) | <a href="https://colab.research.google.com/drive/1DPr4mUQ92Cc-xf4GgAaB6dFcFnWIvqYi?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| 使用 GPTQ 进行 4-bit 量化 | 量化您自己的开源 LLM，使其能在消费级硬件上运行。 | [文章](https://mlabonne.github.io/blog/4bit_quantization/) | <a href="https://colab.research.google.com/drive/1lSvVDaRgqQp_mWK_jC9gydz6_-y6Aq4A?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| 使用 GGUF 和 llama.cpp 进行量化 | 使用 llama.cpp 量化 Llama 2 模型，并将 GGUF 版本上传到 HF Hub。 | [文章](https://mlabonne.github.io/blog/posts/Quantize_Llama_2_models_using_ggml.html) | <a href="https://colab.research.google.com/drive/1pL8k7m04mgE5jo2NrjGi8atB0j_37aDD?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| ExLlamaV2：运行 LLM 最快的库 | 量化并运行 EXL2 模型，并将其上传到 HF Hub。 | [文章](https://mlabonne.github.io/blog/posts/ExLlamaV2_The_Fastest_Library_to_Run%C2%A0LLMs.html) | <a href="https://colab.research.google.com/drive/1yrq4XBlxiA0fALtMoT2dwiACVc77PHou?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |

### 其他

| Notebook | 描述 | 文章 | Notebook |
|---------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| 使用 MergeKit 合并 LLM | 轻松创建您自己的模型，无需 GPU！ | [文章](https://mlabonne.github.io/blog/posts/2024-01-08_Merge_LLMs_with_mergekit%20copy.html) | <a href="https://colab.research.google.com/drive/1_JS7JKJAQozD48-LhYdegcuuZ2ddgXfr?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| 使用 MergeKit 创建 MoE | 将多个专家模型合并成一个 frankenMoE | [文章](https://mlabonne.github.io/blog/posts/2024-03-28_Create_Mixture_of_Experts_with_MergeKit.html) | <a href="https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| 使用 abliteration 解除任意 LLM 的审查 | 无需重新训练的微调 | [文章](https://mlabonne.github.io/blog/posts/2024-06-04_Uncensor_any_LLM_with_abliteration.html) | <a href="https://colab.research.google.com/drive/1VYm3hOcvCpbGiqKZb141gJwjdmmCcVpR?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| 使用知识图谱改进 ChatGPT | 使用知识图谱增强 ChatGPT 的回答。 | [文章](https://mlabonne.github.io/blog/posts/Article_Improve_ChatGPT_with_Knowledge_Graphs.html) | <a href="https://colab.research.google.com/drive/1mwhOSw9Y9bgEaIFKT4CLi0n18pXRM4cj?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |
| 大语言模型中的解码策略 | 从 beam search 到 nucleus sampling 的文本生成指南 | [文章](https://mlabonne.github.io/blog/posts/2022-06-07-Decoding_strategies.html) | <a href="https://colab.research.google.com/drive/19CJlOS5lI29g-B3dziNn93Enez1yiHk2?usp=sharing"><img src="img/colab.svg" alt="在 Colab 中打开"></a> |

## 🧩 LLM 基础

本节介绍关于数学、Python 和神经网络的基础知识。您可能不想从这里开始，但可以在需要时参考。

<details>
<summary>展开/折叠本节 (可选)</summary>
  
![](img/roadmap_fundamentals.png)

### 1. 机器学习数学基础

在掌握机器学习之前，理解支撑这些算法的基础数学概念非常重要。

- **线性代数**: 这对于理解许多算法至关重要，特别是深度学习中使用的算法。关键概念包括向量、矩阵、行列式、特征值和特征向量、向量空间以及线性变换。
- **微积分**: 许多机器学习算法涉及连续函数的优化，这需要理解导数、积分、极限和级数。多元微积分和梯度的概念也很重要。
- **概率与统计**: 这对于理解模型如何从数据中学习并做出预测至关重要。关键概念包括概率论、随机变量、概率分布、期望、方差、协方差、相关性、假设检验、置信区间、最大似然估计和贝叶斯推断。

📚 资源:

- [3Blue1Brown - The Essence of Linear Algebra](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab): 一系列视频，为这些概念提供了几何直觉。
- [StatQuest with Josh Starmer - Statistics Fundamentals](https://www.youtube.com/watch?v=qBigTkBLU6g&list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9): 为许多统计概念提供了简单明了的解释。
- [AP Statistics Intuition by Ms Aerin](https://automata88.medium.com/list/cacc224d5e7d): 一系列 Medium 文章，提供了每种概率分布背后的直觉。
- [Immersive Linear Algebra](https://immersivemath.com/ila/learnmore.html): 线性代数的另一种可视化解释。
- [Khan Academy - Linear Algebra](https://www.khanacademy.org/math/linear-algebra): 非常适合初学者，因为它以非常直观的方式解释了概念。
- [Khan Academy - Calculus](https://www.khanacademy.org/math/calculus-1): 一门互动课程，涵盖了所有微积分基础知识。
- [Khan Academy - Probability and Statistics](https://www.khanacademy.org/math/statistics-probability): 以易于理解的方式提供学习材料。

---

### 2. 机器学习 Python 基础

Python 是一种强大而灵活的编程语言，因其可读性、一致性和强大的数据科学库生态系统，特别适合机器学习。

- **Python 基础**: Python 编程需要对基本语法、数据类型、错误处理和面向对象编程有很好的理解。
- **数据科学库**: 包括熟悉用于数值运算的 NumPy、用于数据操作和分析的 Pandas，以及用于数据可视化的 Matplotlib 和 Seaborn。
- **数据预处理**: 这包括特征缩放和归一化、处理缺失数据、异常值检测、分类数据编码以及将数据拆分为训练集、验证集和测试集。
- **机器学习库**: 熟练使用 Scikit-learn 是至关重要的，它是一个提供多种监督和非监督学习算法的库。理解如何实现线性回归、逻辑回归、决策树、随机森林、K-最近邻 (K-NN) 和 K-均值聚类等算法非常重要。像 PCA 和 t-SNE 这样的降维技术对于可视化高维数据也很有帮助。

📚 资源:

- [Real Python](https://realpython.com/): 一个全面的资源，包含面向初学者和高级用户的 Python 概念文章和教程。
- [freeCodeCamp - Learn Python](https://www.youtube.com/watch?v=rfscVS0vtbw): 一个长视频，全面介绍了 Python 中所有的核心概念。
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/): 一本免费的电子书，是学习 pandas、NumPy、Matplotlib 和 Seaborn 的绝佳资源。
- [freeCodeCamp - Machine Learning for Everybody](https://youtu.be/i_LwzRVP7bg): 为初学者提供的不同机器学习算法的实践介绍。
- [Udacity - Intro to Machine Learning](https://www.udacity.com/course/intro-to-machine-learning--ud120): 一门免费课程，涵盖了 PCA 和其他几个机器学习概念。

---

### 3. 神经网络

神经网络是许多机器学习模型的基础部分，尤其是在深度学习领域。为了有效地利用它们，对它们的设计和机制有全面的了解是必不可少的。

- **基础知识**: 这包括理解神经网络的结构，如层、权重、偏置和激活函数 (sigmoid, tanh, ReLU 等)。
- **训练与优化**: 熟悉反向传播和不同类型的损失函数，如均方误差 (MSE) 和交叉熵。理解各种优化算法，如梯度下降、随机梯度下降、RMSprop 和 Adam。
- **过拟合**: 理解过拟合的概念（即模型在训练数据上表现良好，但在未见过的数据上表现不佳），并学习各种正则化技术（dropout、L1/L2 正则化、早停、数据增强）来防止它。
- **实现多层感知器 (MLP)**: 使用 PyTorch 构建一个 MLP，也称为全连接网络。

📚 资源:

- [3Blue1Brown - But what is a Neural Network?](https://www.youtube.com/watch?v=aircAruvnKk): 这个视频直观地解释了神经网络及其内部工作原理。
- [freeCodeCamp - Deep Learning Crash Course](https://www.youtube.com/watch?v=VyWAvY2CF9c): 这个视频高效地介绍了深度学习中所有最重要的概念。
- [Fast.ai - Practical Deep Learning](https://course.fast.ai/): 专为有编程经验并希望学习深度学习的人设计的免费课程。
- [Patrick Loeber - PyTorch Tutorials](https://www.youtube.com/playlist?list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4): 为完全的初学者学习 PyTorch 而设计的一系列视频。

---

### 4. 自然语言处理 (NLP)

NLP 是人工智能的一个迷人分支，它弥合了人类语言和机器理解之间的鸿沟。从简单的文本处理到理解语言的细微差别，NLP 在翻译、情感分析、聊天机器人等许多应用中扮演着至关重要的角色。

- **文本预处理**: 学习各种文本预处理步骤，如分词（将文本分割成单词或句子）、词干提取（将单词简化为其词根形式）、词形还原（与词干提取类似，但会考虑上下文）、停用词移除等。
- **特征提取技术**: 熟悉将文本数据转换为机器学习算法可以理解的格式的技术。主要方法包括词袋模型 (BoW)、词频-逆文档频率 (TF-IDF) 和 n-grams。
- **词嵌入**: 词嵌入是一种词表示方法，它使得意义相近的词具有相似的表示。主要方法包括 Word2Vec、GloVe 和 FastText。
- **循环神经网络 (RNN)**: 理解 RNN 的工作原理，这是一种为处理序列数据而设计的神经网络。探索 LSTM 和 GRU，这是两种能够学习长期依赖关系的 RNN 变体。

📚 资源:

- [Lena Voita - Word Embeddings](https://lena-voita.github.io/nlp_course/word_embeddings.html): 关于词嵌入相关概念的初学者友好课程。
- [RealPython - NLP with spaCy in Python](https://realpython.com/natural-language-processing-spacy-python/): 关于在 Python 中使用 spaCy 库进行 NLP 任务的详尽指南。
- [Kaggle - NLP Guide](https://www.kaggle.com/learn-guide/natural-language-processing): 一些用于在 Python 中实践解释 NLP 的 notebook 和资源。
- [Jay Alammar - The Illustration Word2Vec](https://jalammar.github.io/illustrated-word2vec/): 理解著名的 Word2Vec 架构的优秀参考资料。
- [Jake Tae - PyTorch RNN from Scratch](https://jaketae.github.io/study/pytorch-rnn/): 在 PyTorch 中对 RNN、LSTM 和 GRU 模型的实用且简单的实现。
- [colah's blog - Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/): 一篇关于 LSTM 网络的更具理论性的文章。
</details>

## 🧑‍🔬 LLM 科学家

本课程的这一部分专注于学习如何使用最新技术构建最好的 LLM。

![](img/roadmap_scientist.png)

### 1. LLM 架构

虽然不需要深入了解 Transformer 架构，但理解现代 LLM 的主要步骤很重要：通过分词将文本转换为数字，通过包括注意力机制在内的层处理这些 token，最后通过各种采样策略生成新文本。

- **架构概述**: 了解从 encoder-decoder Transformer 到像 GPT 这样的 decoder-only 架构的演变，后者构成了现代 LLM 的基础。重点关注这些模型在宏观层面如何处理和生成文本。
- **分词 (Tokenization)**: 学习分词的原理——文本如何被转换成 LLM 可以处理的数值表示。探索不同的分词策略及其对模型性能和输出质量的影响。
- **注意力机制**: 掌握注意力机制的核心概念，特别是自注意力及其变体。理解这些机制如何使 LLM 能够处理长程依赖并在整个序列中保持上下文。
- **采样技术**: 探索各种文本生成方法及其权衡。比较确定性方法（如贪心搜索和束搜索）与概率性方法（如温度采样和核采样）。

📚 **参考资料**:
* [Visual intro to Transformers](https://www.youtube.com/watch?v=wjZofJX0v4M) by 3Blue1Brown: 为完全的初学者提供的 Transformer 可视化入门。
* [LLM Visualization](https://bbycroft.net/llm) by Brendan Bycroft: LLM 内部结构的可交互 3D 可视化。
* [nanoGPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) by Andrej Karpathy: 一个 2 小时长的 YouTube 视频，（为程序员）从零开始重新实现 GPT。他还制作了一个关于[分词](https://www.youtube.com/watch?v=zduSFxRajkE)的视频。
* [Attention? Attention!](https://lilianweng.github.io/posts/2018-06-24-attention/) by Lilian Weng: 介绍注意力机制需求的历史概述。
* [Decoding Strategies in LLMs](https://mlabonne.github.io/blog/posts/2023-06-07-Decoding_strategies.html) by Maxime Labonne: 提供代码和对不同文本生成解码策略的可视化介绍。

---
### 2. 模型预训练

预训练是一个计算密集且昂贵的过程。虽然这不是本课程的重点，但对模型如何进行预训练，尤其是在数据和参数方面有扎实的理解非常重要。业余爱好者也可以用 <1B 的模型进行小规模的预训练。

* **数据准备**: 预训练需要海量数据集（例如，[Llama 3.1](https://arxiv.org/abs/2307.09288) 是在 15 万亿个 token 上训练的），这些数据需要仔细的整理、清洗、去重和分词。现代预训练流程会采用复杂的过滤方法来移除低质量或有问题的内容。
* **分布式训练**: 结合不同的并行化策略：数据并行（批次分布）、流水线并行（层分布）和张量并行（操作拆分）。这些策略需要在 GPU 集群之间进行优化的网络通信和内存管理。
* **训练优化**: 使用带预热的自适应学习率、梯度裁剪和归一化来防止梯度爆炸，使用混合精度训练来提高内存效率，并使用经过调优超参数的现代优化器（AdamW、Lion）。
* **监控**: 使用仪表盘跟踪关键指标（损失、梯度、GPU 状态），为分布式训练问题实现有针对性的日志记录，并设置性能分析以识别跨设备的计算和通信瓶颈。

📚 **参考资料**:
* [FineWeb](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) by Penedo et al.: 一篇关于为 LLM 预训练（15T）重建大规模数据集的文章，包括高质量子集 FineWeb-Edu。
* [RedPajama v2](https://www.together.ai/blog/redpajama-data-v2) by Weber et al.: 另一篇关于大规模预训练数据集的文章和论文，其中包含许多有趣的质量过滤器。
* [nanotron](https://github.com/huggingface/nanotron) by Hugging Face: 用于制作 [SmolLM2](https://github.com/huggingface/smollm) 的极简 LLM 训练代码库。
* [Parallel training](https://www.andrew.cmu.edu/course/11-667/lectures/W10L2%20Scaling%20Up%20Parallel%20Training.pdf) by Chenyan Xiong: 关于优化和并行化技术的概述。
* [Distributed training](https://arxiv.org/abs/2407.20018) by Duan et al.: 关于在分布式架构上高效训练 LLM 的综述。
* [OLMo 2](https://allenai.org/olmo) by AI2: 包含模型、数据、训练和评估代码的开源语言模型。
* [LLM360](https://www.llm360.ai/) by LLM360: 一个用于开源 LLM 的框架，包含训练和数据准备代码、数据、指标和模型。

---
### 3. 后训练数据集

后训练数据集具有精确的结构，包括指令和回答（监督微调）或指令和选择/拒绝的回答（偏好对齐）。对话结构比用于预训练的原始文本要少见得多，这就是为什么我们经常需要处理种子数据并对其进行提炼，以提高样本的准确性、多样性和复杂性。更多信息和示例请见我的仓库 [💾 LLM Datasets](https://github.com/mlabonne/llm-datasets)。

* **存储和聊天模板**: 由于对话结构的存在，后训练数据集以特定格式（如 ShareGPT 或 OpenAI/HF）存储。然后，这些格式被映射到聊天模板（如 ChatML 或 Alpaca），以生成模型训练所用的最终样本。
* **合成数据生成**: 使用前沿模型（如 GPT-4o）基于种子数据创建指令-回答对。这种方法可以灵活、可扩展地创建高质量的答案数据集。关键考虑因素包括设计多样化的种子任务和有效的系统提示。
* **数据增强**: 使用经过验证的输出（使用单元测试或求解器）、带有拒绝采样的多个答案、[Auto-Evol](https://arxiv.org/abs/2406.00770)、思维链 (Chain-of-Thought)、分支-解决-合并 (Branch-Solve-Merge)、角色扮演等技术来增强现有样本。
* **质量过滤**: 传统技术包括基于规则的过滤、使用 MinHash 或 embeddings 删除重复或近似重复的样本，以及 n-gram 去污。奖励模型和裁判 LLM 通过细粒度和可定制的质量控制来补充这一步骤。

📚 **参考资料**:
* [Synthetic Data Generator](https://huggingface.co/spaces/argilla/synthetic-data-generator) by Argilla: 在 Hugging Face Space 中使用自然语言构建数据集的初学者友好方式。
* [LLM Datasets](https://github.com/mlabonne/llm-datasets) by Maxime Labonne: 精选的后训练数据集和工具列表。
* [NeMo-Curator](https://github.com/NVIDIA/NeMo-Curator) by Nvidia: 用于预训练和训练后数据的数据集准备和管理框架。
* [Distilabel](https://distilabel.argilla.io/dev/sections/pipeline_samples/) by Argilla: 用于生成合成数据的框架。它还包括对 UltraFeedback 等论文的有趣复现。
* [Semhash](https://github.com/MinishLab/semhash) by MinishLab: 使用蒸馏嵌入模型进行近乎去重和去污的极简库。
* [Chat Template](https://huggingface.co/docs/transformers/main/en/chat_templating) by Hugging Face: Hugging Face 关于聊天模板的文档。

---
### 4. 监督微调 (Supervised Fine-Tuning)

SFT 将基础模型转变为有用的助手，能够回答问题和遵循指令。在此过程中，它们学习如何构建答案并重新激活在预训练期间学到的部分知识。灌输新知识是可能的，但很肤浅：它不能用于学习一门全新的语言。始终将数据质量置于参数优化之上。

- **训练技术**: 全量微调会更新所有模型参数，但需要大量计算资源。参数高效微调技术如 LoRA 和 QLoRA 通过训练少量适配器参数同时冻结基础权重来减少内存需求。QLoRA 将 4-bit 量化与 LoRA 结合，以减少 VRAM 使用。这些技术都已在最流行的微调框架中实现：[TRL](https://huggingface.co/docs/trl/en/index)、[Unsloth](https://docs.unsloth.ai/) 和 [Axolotl](https://axolotl.ai/)。
- **训练参数**: 关键参数包括带调度器的学习率、批次大小、梯度累积、epoch 数、优化器（如 8-bit AdamW）、用于正则化的权重衰减以及用于训练稳定性的预热步数。LoRA 还增加了三个参数：rank (通常为 16-128)、alpha (rank 的 1-2 倍) 和目标模块。
- **分布式训练**: 使用 DeepSpeed 或 FSDP 在多个 GPU 上扩展训练。DeepSpeed 提供了三个 ZeRO 优化阶段，通过状态分区实现不同程度的内存效率提升。两种方法都支持梯度检查点以提高内存效率。
- **监控**: 跟踪训练指标，包括损失曲线、学习率调度和梯度范数。监控常见问题，如损失尖峰、梯度爆炸或性能下降。

📚 **参考资料**:
* [Fine-tune Llama 3.1 Ultra-Efficiently with Unsloth](https://huggingface.co/blog/mlabonne/sft-llama3) by Maxime Labonne: 关于如何使用 Unsloth 微调 Llama 3.1 模型的实践教程。
* [Axolotl - Documentation](https://axolotl-ai-cloud.github.io/axolotl/) by Wing Lian: 大量关于分布式训练和数据集格式的有趣信息。
* [Mastering LLMs](https://parlance-labs.com/education/) by Hamel Husain: 关于微调（以及 RAG、评估、应用和提示工程）的教育资源集合。
* [LoRA insights](https://lightning.ai/pages/community/lora-insights/) by Sebastian Raschka: 关于 LoRA 以及如何选择最佳参数的实践见解。

---
### 5. 偏好对齐 (Preference Alignment)

偏好对齐是训练后流程的第二阶段，专注于使生成的答案与人类偏好保持一致。这一阶段旨在调整 LLM 的语气，并减少毒性和幻觉。然而，它也变得越来越重要，以提升其性能和实用性。与 SFT 不同，有许多偏好对齐算法。在这里，我们将重点关注三个最重要的算法：DPO、GRPO 和 PPO。

- **拒绝采样**: 对每个提示，使用训练好的模型生成多个响应，并对它们进行评分以推断出被选择/被拒绝的答案。这会创建 on-policy 数据，其中两个响应都来自正在训练的模型，从而提高了对齐的稳定性。
- **[直接偏好优化 (DPO)](https://arxiv.org/abs/2305.18290)**: 直接优化策略以最大化选择的响应相对于被拒绝的响应的似然。它不需要奖励建模，这使得它比 RL 技术计算效率更高，但在质量上稍差。非常适合创建聊天模型。
- **奖励模型**: 使用人类反馈训练一个奖励模型，以预测人类偏好等指标。它可以利用 [TRL](https://huggingface.co/docs/trl/en/index)、[verl](https://github.com/volcengine/verl) 和 [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) 等框架进行可扩展的训练。
- **强化学习**: RL 技术如 [GRPO](https://arxiv.org/abs/2402.03300) 和 [PPO](https://arxiv.org/abs/1707.06347) 迭代地更新策略以最大化奖励，同时保持与初始行为的接近。它们可以使用奖励模型或奖励函数来对响应进行评分。它们往往计算成本高昂，需要仔细调整超参数，包括学习率、批次大小和裁剪范围。非常适合创建推理模型。

📚 **参考资料**:
* [Illustrating RLHF](https://huggingface.co/blog/rlhf) by Hugging Face: 介绍 RLHF，包括奖励模型训练和使用强化学习进行微调。
* [LLM Training: RLHF and Its Alternatives](https://magazine.sebastianraschka.com/p/llm-training-rlhf-and-its-alternatives) by Sebastian Raschka: RLHF 过程及其替代方案（如 RLAIF）的概述。
* [Preference Tuning LLMs](https://huggingface.co/blog/pref-tuning) by Hugging Face: DPO、IPO 和 KTO 等偏好对齐算法的比较。
* [Fine-tune with DPO](https://mlabonne.github.io/blog/posts/Fine_tune_Mistral_7b_with_DPO.html) by Maxime Labonne: 使用 DPO 微调 Mistral-7b 模型并复现 [NeuralHermes-2.5](https://huggingface.co/mlabonne/NeuralHermes-2.5-Mistral-7B) 的教程。
* [Fine-tune with GRPO](https://huggingface.co/learn/llm-course/en/chapter12/5) by Maxime Labonne: 使用 GRPO 微调小型模型的实践练习。
* [DPO Wandb logs](https://wandb.ai/alexander-vishnevskiy/dpo/reports/TRL-Original-DPO--Vmlldzo1NjI4MTc4) by Alexander Vishnevskiy: 展示了需要跟踪的主要 DPO 指标以及您应该预期的趋势。

---
### 6. 评估

可靠地评估 LLM 是一项复杂但至关重要的任务，它指导着数据生成和训练。它为改进领域提供了宝贵的反馈，可用于修改数据混合、质量和训练参数。然而，始终要记住古德哈特定律：“当一个度量成为目标时，它就不再是一个好的度量。”

- **自动化基准测试**: 使用精选的数据集和指标（如 MMLU）评估模型在特定任务上的表现。它在具体任务上效果很好，但在抽象和创造性能力方面表现不佳。它也容易受到数据污染的影响。
- **人工评估**: 包括由人类向模型提问并对响应进行评分。方法从“感觉”检查到使用特定指南和大规模社区投票（竞技场）的系统性标注。它更适合主观任务，而在事实准确性方面不太可靠。
- **基于模型的评估**: 使用裁判和奖励模型来评估模型输出。它与人类偏好高度相关，但存在偏向于自身输出和评分不一致的问题。
- **反馈信号**: 分析错误模式以识别特定弱点，例如遵循复杂指令的限制、缺乏特定知识或易受对抗性提示影响。这可以通过更好的数据生成和训练参数来改进。

📚 **参考资料**:
* [Evaluation guidebook](https://github.com/huggingface/evaluation-guidebook) by Clémentine Fourrier: 关于 LLM 评估的实践见解和理论知识。
* [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) by Hugging Face: 以开放和可复现的方式比较 LLM 的主要排行榜（自动化基准测试）。
* [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) by EleutherAI: 一个用于使用自动化基准测试评估 LLM 的流行框架。
* [Lighteval](https://github.com/huggingface/lighteval) by Hugging Face: 另一个评估框架，也包括基于模型的评估。
* [Chatbot Arena](https://lmarena.ai/) by LMSYS: 通用 LLM 的 Elo 评级，基于人类的比较（人工评估）。

---
### 7. 量化

量化是使用较低精度转换模型参数和激活值的过程。例如，使用 16 位存储的权重可以转换为 4 位表示。这项技术对于降低与 LLM 相关的计算和内存成本变得越来越重要。

* **基础技术**: 学习不同级别的精度（FP32、FP16、INT8 等）以及如何使用 absmax 和零点技术进行朴素量化。
* **GGUF 和 llama.cpp**: 最初设计用于在 CPU 上运行，[llama.cpp](https://github.com/ggerganov/llama.cpp) 和 GGUF 格式已成为在消费级硬件上运行 LLM 最流行的工具。它支持在单个文件中存储特殊 token、词汇表和元数据。
* **GPTQ 和 AWQ**: 像 [GPTQ](https://arxiv.org/abs/2210.17323)/[EXL2](https://github.com/turboderp/exllamav2) 和 [AWQ](https://arxiv.org/abs/2306.00978) 这样的技术引入了逐层校准，从而在极低的比特宽度下保持性能。它们通过动态缩放、选择性地跳过或重新中心化最重的参数来减少灾难性异常值。
* **SmoothQuant 和 ZeroQuant**: 新的量化友好转换（SmoothQuant）和基于编译器的优化（ZeroQuant）有助于在量化前减轻异常值。它们还通过融合某些操作和优化数据流来减少硬件开销。

📚 **参考资料**:
* [Introduction to quantization](https://mlabonne.github.io/blog/posts/Introduction_to_Weight_Quantization.html) by Maxime Labonne: 量化、absmax 和零点量化以及 LLM.int8() 的概述及代码。
* [Quantize Llama models with llama.cpp](https://mlabonne.github.io/blog/posts/Quantize_Llama_2_models_using_ggml.html) by Maxime Labonne: 关于如何使用 llama.cpp 和 GGUF 格式量化 Llama 2 模型的教程。
* [4-bit LLM Quantization with GPTQ](https://mlabonne.github.io/blog/posts/4_bit_Quantization_with_GPTQ.html) by Maxime Labonne: 关于如何使用 GPTQ 算法和 AutoGPTQ 量化 LLM 的教程。
* [Understanding Activation-Aware Weight Quantization](https://medium.com/friendliai/understanding-activation-aware-weight-quantization-awq-boosting-inference-serving-efficiency-in-10bb0faf63a8) by FriendliAI: AWQ 技术及其优势的概述。
* [SmoothQuant on Llama 2 7B](https://github.com/mit-han-lab/smoothquant/blob/main/examples/smoothquant_llama_demo.ipynb) by MIT HAN Lab: 关于如何在 Llama 2 模型上以 8-bit 精度使用 SmoothQuant 的教程。
* [DeepSpeed Model Compression](https://www.deepspeed.ai/tutorials/model-compression/) by DeepSpeed: 关于如何使用 DeepSpeed Compression 进行 ZeroQuant 和极端压缩（XTC）的教程。

---
### 8. 新趋势

这里是一些未归入其他类别的值得关注的主题。有些是成熟的技术（模型合并、多模态），但其他一些则更具实验性（可解释性、测试时计算扩展），并且是众多研究论文的焦点。

* **模型合并**: 合并训练好的模型已成为一种无需任何微调即可创建高性能模型的流行方式。流行的 [mergekit](https://github.com/cg123/mergekit) 库实现了最流行的合并方法，如 SLERP、[DARE](https://arxiv.org/abs/2311.03099) 和 [TIES](https://arxiv.org/abs/2311.03099)。
* **多模态模型**: 这些模型（如 [CLIP](https://openai.com/research/clip)、[Stable Diffusion](https://stability.ai/stable-image) 或 [LLaVA](https://llava-vl.github.io/)）使用统一的嵌入空间处理多种类型的输入（文本、图像、音频等），从而解锁了像文本到图像这样强大的应用。
* **可解释性**: 像稀疏自动编码器（SAE）这样的机制性可解释性技术在提供关于 LLM 内部工作原理的见解方面取得了显著进展。这也被应用于像 abliteration 这样的技术，它允许您在不进行训练的情况下修改模型的行为。
* **测试时计算**: 使用 RL 技术训练的推理模型可以通过在测试时扩展计算预算来进一步改进。这可能涉及多次调用、MCTS 或像过程奖励模型（PRM）这样的专门模型。使用精确评分的迭代步骤显著提高了复杂推理任务的性能。

📚 **参考资料**:
* [Merge LLMs with mergekit](https://mlabonne.github.io/blog/posts/2024-01-08_Merge_LLMs_with_mergekit.html) by Maxime Labonne: 关于使用 mergekit 进行模型合并的教程。
* [Smol Vision](https://github.com/merveenoyan/smol-vision) by Merve Noyan: 专用于小型多模态模型的 notebook 和脚本集合。
* [Large Multimodal Models](https://huyenchip.com/2023/10/10/multimodal.html) by Chip Huyen: 多模态系统及该领域近期历史的概述。
* [Unsensor any LLM with abliteration](https://huggingface.co/blog/mlabonne/abliteration) by Maxime Labonne: 直接应用可解释性技术来修改模型风格。
* [Intuitive Explanation of SAEs](https://adamkarvonen.github.io/machine_learning/2024/06/11/sae-intuitions.html) by Adam Karvonen: 关于 SAEs 如何工作以及为什么它们对可解释性有意义的文章。
* [Scaling test-time compute](https://huggingface.co/spaces/HuggingFaceH4/blogpost-scaling-test-time-compute) by Beeching et al.: 使用 3B 模型在 MATH-500 上超越 Llama 3.1 70B 的教程和实验。

## 👷 LLM 工程师

本课程的这一部分专注于学习如何构建可用于生产环境的 LLM 驱动的应用程序，重点是增强模型和部署模型。

![](img/roadmap_engineer.png)

### 1. 运行 LLM

由于硬件要求高，运行 LLM 可能很困难。根据您的用例，您可能只想通过 API（如 GPT-4）使用模型，或者在本地运行它。在任何情况下，额外的提示和指导技术都可以改进和约束您的应用程序的输出。

* **LLM API**: API 是部署 LLM 的一种便捷方式。这个领域分为私有 LLM（[OpenAI](https://platform.openai.com/)、[Google](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/overview)、[Anthropic](https://docs.anthropic.com/claude/reference/getting-started-with-the-api) 等）和开源 LLM（[OpenRouter](https://openrouter.ai/)、[Hugging Face](https://huggingface.co/inference-api)、[Together AI](https://www.together.ai/) 等）。
* **开源 LLM**: [Hugging Face Hub](https://huggingface.co/models) 是寻找 LLM 的好地方。您可以直接在 [Hugging Face Spaces](https://huggingface.co/spaces) 中运行其中一些模型，或者下载并在本地应用程序（如 [LM Studio](https://lmstudio.ai/)）中运行，或者通过 CLI 使用 [llama.cpp](https://github.com/ggerganov/llama.cpp) 或 [ollama](https://ollama.ai/) 运行。
* **提示工程**: 常用技术包括零样本提示 (zero-shot prompting)、少样本提示 (few-shot prompting)、思维链 (chain of thought) 和 ReAct。它们在更大的模型上效果更好，但也可以适应较小的模型。
* **结构化输出**: 许多任务需要结构化输出，如严格的模板或 JSON 格式。像 [Outlines](https://github.com/outlines-dev/outlines) 这样的库可以用来引导生成并遵循给定的结构。一些 API 也支持使用 JSON schema 原生生成结构化输出。

📚 **参考资料**:
* [Run an LLM locally with LM Studio](https://www.kdnuggets.com/run-an-llm-locally-with-lm-studio) by Nisha Arya: 关于如何使用 LM Studio 的简短指南。
* [Prompt engineering guide](https://www.promptingguide.ai/) by DAIR.AI: 包含示例的详尽提示技术列表。
* [Outlines - Quickstart](https://dottxt-ai.github.io/outlines/latest/quickstart/): Outlines 支持的引导生成技术列表。
* [LMQL - Overview](https://lmql.ai/docs/language/overview.html): LMQL 语言简介。

---
### 2. 构建向量存储

创建向量存储是构建检索增强生成（RAG）流程的第一步。文档被加载、分割，相关的块被用来生成向量表示（嵌入），这些嵌入被存储起来以备推理时使用。

* **文档摄取**: 文档加载器是方便的包装器，可以处理多种格式：PDF、JSON、HTML、Markdown 等。它们还可以直接从一些数据库和 API（GitHub、Reddit、Google Drive 等）中检索数据。
* **文档分割**: 文本分割器将文档分解成更小的、有语义意义的块。与其在 *n* 个字符后分割文本，不如按标题或递归地分割，并附带一些额外的元数据，效果通常更好。
* **嵌入模型**: 嵌入模型将文本转换为向量表示。选择特定于任务的模型可以显著提高语义搜索和 RAG 的性能。
* **向量数据库**: 向量数据库（如 [Chroma](https://www.trychroma.com/)、[Pinecone](https://www.pinecone.io/)、[Milvus](https://milvus.io/)、[FAISS](https://faiss.ai/)、[Annoy](https://github.com/spotify/annoy) 等）被设计用于存储嵌入向量。它们能够基于向量相似性高效地检索与查询“最相似”的数据。

📚 **参考资料**:
* [LangChain - Text splitters](https://python.langchain.com/docs/how_to/#text-splitters): LangChain 中实现的不同文本分割器列表。
* [Sentence Transformers library](https://www.sbert.net/): 流行的嵌入模型库。
* [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard): 嵌入模型的排行榜。
* [The Top 7 Vector Databases](https://www.datacamp.com/blog/the-top-5-vector-databases) by Moez Ali: 最好和最流行的向量数据库的比较。

---
### 3. 检索增强生成 (RAG)

通过 RAG，LLM 从数据库中检索上下文文档以提高其答案的准确性。RAG 是一种无需任何微调即可增强模型知识的流行方法。

* **编排器**:像 [LangChain](https://python.langchain.com/docs/get_started/introduction) 和 [LlamaIndex](https://docs.llamaindex.ai/en/stable/) 这样的编排器是连接您的 LLM 与工具和数据库的流行框架。模型上下文协议 (MCP) 引入了一个新标准，用于跨提供商向模型传递数据和上下文。
* **检索器**: 查询重写器和生成式检索器（如 CoRAG 和 HyDE）通过转换用户查询来增强搜索。多向量和混合检索方法将嵌入与关键字信号相结合，以提高召回率和精确度。
* **记忆**: 为了记住之前的指令和答案，LLM 和像 ChatGPT 这样的聊天机器人会将这段历史添加到它们的上下文窗口中。这个缓冲区可以通过摘要（例如，使用一个较小的 LLM）、向量存储 + RAG 等方式进行改进。
* **评估**: 我们需要评估文档检索（上下文精确度和召回率）和生成阶段（忠实度和答案相关性）。这可以通过工具 [Ragas](https://github.com/explodinggradients/ragas/tree/main) 和 [DeepEval](https://github.com/confident-ai/deepeval)（评估质量）来简化。

📚 **参考资料**:
* [Llamaindex - High-level concepts](https://docs.llamaindex.ai/en/stable/getting_started/concepts.html): 构建 RAG 流程时需要了解的主要概念。
* [Model Context Protocol](https://modelcontextprotocol.io/introduction): MCP 的介绍，包括动机、架构和快速入门。
* [Pinecone - Retrieval Augmentation](https://www.pinecone.io/learn/series/langchain/langchain-retrieval-augmentation/): 检索增强过程的概述。
* [LangChain - Q&A with RAG](https://python.langchain.com/docs/tutorials/rag/): 构建典型 RAG 流程的分步教程。
* [LangChain - Memory types](https://python.langchain.com/docs/how_to/chatbots_memory/): 不同类型记忆的列表及其相关用法。
* [RAG pipeline - Metrics](https://docs.ragas.io/en/stable/concepts/metrics/index.html): 用于评估 RAG 流程的主要指标概述。

---
### 4. 高级 RAG

现实世界的应用程序可能需要复杂的流程，包括 SQL 或图数据库，以及自动选择相关工具和 API。这些先进技术可以改进基线解决方案并提供附加功能。

* **查询构建**: 存储在传统数据库中的结构化数据需要特定的查询语言，如 SQL、Cypher、元数据等。我们可以直接将用户指令翻译成查询来访问数据，这就是查询构建。
* **工具**: Agent 通过自动选择最相关的工具来提供答案，从而增强 LLM。这些工具可以像使用 Google 或维基百科一样简单，也可以像 Python 解释器或 Jira 一样复杂。
* **后处理**: 处理输入到 LLM 的内容的最后一步。它通过重排、[RAG-fusion](https://github.com/Raudaschl/rag-fusion) 和分类来增强检索到的文档的相关性和多样性。
* **编程 LLM**: 像 [DSPy](https://github.com/stanfordnlp/dspy) 这样的框架允许您以编程方式，基于自动化评估来优化提示和权重。

📚 **参考资料**:
* [LangChain - Query Construction](https://blog.langchain.dev/query-construction/): 关于不同类型查询构建的博客文章。
* [LangChain - SQL](https://python.langchain.com/docs/tutorials/sql_qa/): 关于如何与 SQL 数据库与 LLM 交互的教程，涉及 Text-to-SQL 和一个可选的 SQL agent。
* [Pinecone - LLM agents](https://www.pinecone.io/learn/series/langchain/langchain-agents/): 介绍不同类型的 agent 和工具。
* [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) by Lilian Weng: 一篇关于 LLM agent 的更具理论性的文章。
* [LangChain - OpenAI's RAG](https://blog.langchain.dev/applying-openai-rag/): OpenAI 使用的 RAG 策略概述，包括后处理。
* [DSPy in 8 Steps](https://dspy-docs.vercel.app/docs/building-blocks/solving_your_task): DSPy 的通用指南，介绍模块、签名和优化器。

---
### 5. Agent

LLM Agent 可以通过基于对其环境的推理采取行动来自主执行任务，通常通过使用工具或函数与外部系统交互。

* **Agent 基础**: Agent 通过思考（决定下一步做什么的内部推理）、行动（执行任务，通常通过与外部工具交互）和观察（分析反馈或结果以完善下一步）来运作。
* **Agent 框架**: Agent 开发可以通过不同的框架来简化，例如 [LangGraph](https://www.langchain.com/langgraph)（工作流的设计和可视化）、[LlamaIndex](https://docs.llamaindex.ai/en/stable/use_cases/agents/)（使用 RAG 的数据增强 Agent）或 [smolagents](https://github.com/huggingface/smolagents)（初学者友好、轻量级的选项）。
* **多 Agent**: 更具实验性的框架包括不同 Agent 之间的协作，例如 [CrewAI](https://docs.crewai.com/introduction)（基于角色的团队协调）、[AutoGen](https://github.com/microsoft/autogen)（对话驱动的多 Agent 系统）和 [OpenAI Agents SDK](https://github.com/openai/openai-agents-python)（生产就绪，与 OpenAI 模型强集成）。

📚 **参考资料**:
* [Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction): 由 Hugging Face 制作的关于 AI agent 的热门课程。
* [AI Agents Comparison](https://langfuse.com/blog/2025-03-19-ai-agent-comparison) by Jannik Maierhöfer: 不同开源 AI agent 框架的功能比较。
* [LangGraph](https://langchain-ai.github.io/langgraph/concepts/why-langgraph/): 关于如何使用 LangGraph 构建 AI agent 的概述。
* [LlamaIndex Agents](https://docs.llamaindex.ai/en/stable/use_cases/agents/): 使用 LlamaIndex 构建 Agent 的用例和资源。
* [smolagents](https://huggingface.co/docs/smolagents/index): 包含导览、操作指南和更多概念性文章的文档。

---
### 6. 推理优化

文本生成是一个昂贵的过程，需要昂贵的硬件。除了量化之外，还提出了各种技术来最大化吞吐量和降低推理成本。

* **Flash Attention**: 对注意力机制的优化，将其复杂度从二次方降为线性，从而加速训练和推理。
* **键值缓存**: 理解键值缓存以及在 [Multi-Query Attention](https://arxiv.org/abs/1911.02150) (MQA) 和 [Grouped-Query Attention](https://arxiv.org/abs/2305.13245) (GQA) 中引入的改进。
* **推测解码**: 使用一个小型模型生成草稿，然后由一个大型模型进行审查，以加速文本生成。

📚 **参考资料**:
* [GPU Inference](https://huggingface.co/docs/transformers/main/en/perf_infer_gpu_one) by Hugging Face: 解释如何优化 GPU 上的推理。
* [LLM Inference](https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices) by Databricks: 在生产中优化 LLM 推理的最佳实践。
* [Optimizing LLMs for Speed and Memory](https://huggingface.co/docs/transformers/main/en/llm_tutorial_optimization) by Hugging Face: 解释优化速度和内存的三种主要技术，即量化、Flash Attention 和架构创新。
* [Assisted Generation](https://huggingface.co/blog/assisted-generation) by Hugging Face: HF 版本的推测解码，这是一篇关于其工作原理及实现代码的有趣博客文章。

---
### 7. 部署 LLM

大规模部署 LLM 是一项工程壮举，可能需要多个 GPU 集群。在其他情况下，演示和本地应用程序可以用低得多的复杂性来实现。

* **本地部署**: 隐私是开源 LLM 相对于私有 LLM 的一个重要优势。本地 LLM 服务器（[LM Studio](https://lmstudio.ai/)、[Ollama](https://ollama.ai/)、[oobabooga](https://github.com/oobabooga/text-generation-webui)、[kobold.cpp](https://github.com/LostRuins/koboldcpp) 等）利用这一优势为本地应用程序提供支持。
* **演示部署**: 像 [Gradio](https://www.gradio.app/) 和 [Streamlit](https://docs.streamlit.io/) 这样的框架有助于原型化应用程序和共享演示。您还可以轻松地将它们托管在网上，例如使用 [Hugging Face Spaces](https://huggingface.co/spaces)。
* **服务器部署**: 大规模部署 LLM 需要云（另请参阅 [SkyPilot](https://skypilot.readthedocs.io/en/latest/)）或本地基础设施，并经常利用优化的文本生成框架，如 [TGI](https://github.com/huggingface/text-generation-inference)、[vLLM](https://github.com/vllm-project/vllm/tree/main) 等。
* **边缘部署**: 在受限环境中，像 [MLC LLM](https://github.com/mlc-ai/mlc-llm) 和 [mnn-llm](https://github.com/wangzhaode/mnn-llm/blob/master/README_en.md) 这样的高性能框架可以在 Web 浏览器、Android 和 iOS 上部署 LLM。

📚 **参考资料**:
* [Streamlit - Build a basic LLM app](https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps): 使用 Streamlit 制作一个基本的类 ChatGPT 应用程序的教程。
* [HF LLM Inference Container](https://huggingface.co/blog/sagemaker-huggingface-llm): 使用 Hugging Face 的推理容器在 Amazon SageMaker 上部署 LLM。
* [Philschmid blog](https://www.philschmid.de/) by Philipp Schmid: 关于使用 Amazon SageMaker 部署 LLM 的高质量文章集合。
* [Optimizing latence](https://hamel.dev/notes/llm/inference/03_inference.html) by Hamel Husain: TGI、vLLM、CTranslate2 和 mlc 在吞吐量和延迟方面的比较。

---
### 8. LLM 安全

除了与软件相关的传统安全问题外，LLM 由于其训练和提示方式而存在独特的弱点。

* **提示攻击**: 与提示工程相关的不同技术，包括提示注入（附加指令以劫持模型回答）、数据/提示泄露（检索其原始数据/提示）和越狱（精心设计提示以绕过安全功能）。
* **后门**: 攻击向量可以针对训练数据本身，通过毒化训练数据（例如，使用虚假信息）或创建后门（在推理期间改变模型行为的秘密触发器）。
* **防御措施**: 保护您的 LLM 应用程序的最佳方法是测试它们以防范这些漏洞（例如，使用红队测试和像 [garak](https://github.com/leondz/garak/) 这样的检查），并在生产中观察它们（使用像 [langfuse](https://github.com/langfuse/langfuse) 这样的框架）。

📚 **参考资料**:
* [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) by HEGO Wiki: LLM 应用程序中看到的 10 个最关键漏洞列表。
* [Prompt Injection Primer](https://github.com/jthack/PIPE) by Joseph Thacker: 为工程师准备的关于提示注入的简短指南。
* [LLM Security](https://llmsecurity.net/) by [@llm_sec](https://twitter.com/llm_sec): 与 LLM 安全相关的广泛资源列表。
* [Red teaming LLMs](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/red-teaming) by Microsoft: 关于如何对 LLM 进行红队测试的指南。

---
## 致谢

这个学习路线图的灵感来自于 Milan Milanović 和 Romano Roth 出色的 [DevOps Roadmap](https://github.com/milanm/DevOps-Roadmap)。

特别感谢：

* Thomas Thelen 激励我创建这个路线图
* André Frade 对初稿的意见和审阅
* Dino Dunn 提供有关 LLM 安全的资源
* Magdalena Kuhn 改进了“人工评估”部分
* Odoverdose 建议了 3Blue1Brown 关于 Transformer 的视频
* 所有为本课程中的教育参考资料做出贡献的人 :)

*免责声明：我与此处列出的任何来源均无附属关系。*

---

[![Star History Chart](https://api.star-history.com/svg?repos=mlabonne/llm-course&type=Date)](https://www.star-history.com/#mlabonne/llm-course&Date)
