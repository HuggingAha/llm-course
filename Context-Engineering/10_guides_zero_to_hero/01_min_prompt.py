#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最小提示探索：上下文工程基础
==============================================================

本脚本通过探索最小、原子的提示词，介绍上下文工程的核心原理，并观察其对大语言模型（LLM）输出和行为的直接影响。

主要涵盖内容：
1. 构建原子级提示词，实现最大清晰度与可控性
2. 通过 token 数和模型响应质量衡量有效性
3. 迭代修改提示词，实现快速反馈循环
4. 观察上下文漂移和最小提示边界
5. 为从原子提示扩展到协议化外壳打下基础

用法：
    # 在 Jupyter 或 Colab 中：
    %run 01_min_prompt.py
    # 或
    # 可独立编辑和运行每个部分，实验提示词效果

注意：
    - 本脚本每个部分都适合动手实验。
    - 可修改提示词，观察分词和输出保真度的变化。
    - 可作为进阶上下文工程工作流的基础。

"""


import os
import time
import json
from typing import Dict, List, Any, Tuple, Optional
import matplotlib.pyplot as plt

# 如果你使用 OpenAI 的 API，取消注释下方并设置你的 API 密钥
# import openai
# openai.api_key = os.getenv("OPENAI_API_KEY")  # 建议将 API 密钥设置为环境变量

# 如使用其他厂商，请相应调整
# 以下为演示用的简易 LLM 类
class SimpleLLM:
    """最简 LLM 接口，仅用于演示。"""
    
    def __init__(self, model_name: str = "dummy-model"):
        """初始化 LLM 接口。"""
        self.model_name = model_name
        self.total_tokens_used = 0  # 累计 token 数
        self.total_requests = 0  # 累计请求次数

    def count_tokens(self, text: str) -> int:
        """
        用极其简单的方式统计文本 token 数。
        实际生产中应使用模型专用的分词器。
        """
        # 这里只是粗略估算，实际应用请用专业分词器
        return len(text.split())
    
    def generate(self, prompt: str) -> str:
        """
        根据提示词生成文本（演示用假实现）。
        实际应用中应调用真实的 LLM API。
        """
        # 实际实现应调用 API
        # response = openai.ChatCompletion.create(
        #     model="gpt-4",
        #     messages=[{"role": "user", "content": prompt}]
        # )
        # return response.choices[0].message.content

        # 演示用，仅返回提示词 token 数
        tokens = self.count_tokens(prompt)
        self.total_tokens_used += tokens
        self.total_requests += 1

        return f"[此处为 LLM 响应内容。你的提示词大约用了 {tokens} 个 token。]"
    
    def get_stats(self) -> Dict[str, Any]:
        """返回使用统计信息。"""
        return {
            "total_tokens": self.total_tokens_used,
            "total_requests": self.total_requests,
            "avg_tokens_per_request": self.total_tokens_used / max(1, self.total_requests)
        }

# 初始化 LLM 接口
llm = SimpleLLM()

# ----- 实验1：原子级提示词 -----
print("\n----- EXPERIMENT 1: THE ATOMIC PROMPT -----")
print("让我们从最基本的单条指令开始。")

atomic_prompt = "Write a short poem about programming."
tokens = llm.count_tokens(atomic_prompt)

print(f"\nAtomic Prompt: '{atomic_prompt}'")
print(f"Token Count: {tokens}")
print("\nGenerating response...")
response = llm.generate(atomic_prompt)
print(f"\nResponse:\n{response}")

# ----- 实验2：添加约束 -----
print("\n----- EXPERIMENT 2: ADDING CONSTRAINTS -----")
print("现在我们为原子提示词添加约束，观察变化。")

# 创建三种不同约束的提示词
prompts = [
    "Write a short poem about programming.",  # 原始
    "Write a short poem about programming in 4 lines.",  # 增加长度约束
    "Write a short haiku about programming using only simple words.",  # 增加格式和词汇约束
]

# 统计 token 并生成响应
results = []
for i, prompt in enumerate(prompts):
    tokens = llm.count_tokens(prompt)
    print(f"\nPrompt {i+1}: '{prompt}'")
    print(f"Token Count: {tokens}")
    
    start_time = time.time()
    response = llm.generate(prompt)
    end_time = time.time()
    
    results.append({
        "prompt": prompt,
        "tokens": tokens,
        "response": response,
        "latency": end_time - start_time
    })
    
    print(f"Latency: {results[-1]['latency']:.4f} seconds")
    print(f"Response:\n{response}")

# ----- 实验3：ROI 曲线测量 -----
print("\n----- EXPERIMENT 3: MEASURING THE ROI CURVE -----")
print("探索提示词复杂度与输出质量的关系。")

# 实际应用中应为每个响应定义主观质量分数
# 此处为演示，使用占位分数
quality_scores = [3, 6, 8]  # 1-10分主观分数

# 绘制 token 数与质量的关系曲线
plt.figure(figsize=(10, 6))
tokens_list = [r["tokens"] for r in results]
plt.plot(tokens_list, quality_scores, marker='o', linestyle='-', color='blue')
plt.xlabel('Tokens in Prompt')
plt.ylabel('Output Quality (1-10)')
plt.title('Token-Quality ROI Curve')
plt.grid(True)

# 添加注释
for i, (x, y) in enumerate(zip(tokens_list, quality_scores)):
    plt.annotate(f"Prompt {i+1}", (x, y), textcoords="offset points", 
                 xytext=(0, 10), ha='center')

# Jupyter 环境下可显示图表
# plt.show()
print("[Jupyter 环境下此处会显示图表]")

# ----- 实验4：最小上下文增强 -----
print("\n----- EXPERIMENT 4: MINIMAL CONTEXT ENHANCEMENT -----")
print("现在我们在保持 token 数较低的前提下，添加最小上下文以提升输出质量。")

# 构造带有策略性上下文的提示词
enhanced_prompt = """Task: Write a haiku about programming.

A haiku is a three-line poem with 5, 7, and 5 syllables per line.
Focus on the feeling of solving a difficult bug."""

tokens = llm.count_tokens(enhanced_prompt)
print(f"\nEnhanced Prompt:\n'{enhanced_prompt}'")
print(f"Token Count: {tokens}")

response = llm.generate(enhanced_prompt)
print(f"\nResponse:\n{response}")

# ----- 实验5：一致性测量 -----
print("\n----- EXPERIMENT 5: MEASURING CONSISTENCY -----")
print("测试最小提示与增强提示下输出的一致性。")

# 生成多次响应并测量一致性
# 实际应用中可用语义相似度等指标
# 这里只做演示

def measure_consistency(prompt: str, n_samples: int = 3) -> Dict[str, Any]:
    """多次生成响应并测量一致性（演示用）。"""
    responses = []
    total_tokens = 0
    
    for _ in range(n_samples):
        response = llm.generate(prompt)
        responses.append(response)
        total_tokens += llm.count_tokens(prompt)

    # 实际应实现更科学的一致性度量
    consistency_score = 0.5  # 占位分数

    return {
        "prompt": prompt,
        "responses": responses,
        "total_tokens": total_tokens,
        "consistency_score": consistency_score
    }

# 对比基础提示与增强提示
basic_results = measure_consistency(prompts[0])
enhanced_results = measure_consistency(enhanced_prompt)

print(f"\nBasic Prompt Consistency Score: {basic_results['consistency_score']}")
print(f"Enhanced Prompt Consistency Score: {enhanced_results['consistency_score']}")

# ----- 结论 -----
print("\n----- CONCLUSION -----")
print("实验总结：")
print("1. 即使是很小的提示词调整也会显著影响输出质量")
print("2. token 数与质量之间存在 ROI 曲线，需平衡")
print("3. 添加策略性上下文可提升一致性")
print("4. 最佳提示词应清晰、简洁并提供恰到好处的上下文")

print("\nTotal tokens used in this notebook:", llm.get_stats()["total_tokens"])

# ----- 后续建议 -----
print("\n----- NEXT STEPS -----")
print("1. 用真实 LLM API 进行实验")
print("2. 实现更科学的一致性与质量度量")
print("3. 探索“分子”概念——组合多条指令")
print("4. 尝试 few-shot 示例在上下文窗口中的效果")

"""
读者练习：

1. 将本脚本接入真实 LLM API（如 OpenAI、Anthropic 等）
2. 用不同模型尺寸测试同一组提示词
3. 针对你关心的任务绘制自己的 token-质量曲线
4. 找到你场景下的“最小可用上下文”

进阶内容见 02_expand_context.ipynb。
"""

# 如在 Jupyter 环境下，可将结果保存到文件
# with open('experiment_results.json', 'w') as f:
#     json.dump(results, f, indent=2)
