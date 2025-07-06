# 高级应用：让上下文工程落地

> “理论上，理论和实践是一样的。但实际上，它们并不一样。”——爱因斯坦

## 超越基础：应用型上下文工程

我们已经构建了坚实的上下文工程基础，从原子提示到认知工具。现在，是时候看看这些原则如何应用于推动 LLM 能力边界的真实挑战。

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│              │     │              │     │              │     │              │
│    原子      │────►│   分子       │────►│    细胞      │────►│    器官      │
│   (提示)     │     │ (少样本)     │     │   (记忆)     │     │ (多智能体)   │
│              │     │              │     │              │     │              │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
       │                    │                   │                    │
       │                    │                   │                    │
       │                    │                   │                    │
       ▼                    ▼                   ▼                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│                         高级应用                                             │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

## 应用领域：长文本内容创作

创作连贯的长文本内容极大考验上下文管理。让我们看看这些原则如何落地：

```
┌───────────────────────────────────────────────────────────────────────────┐
│                    长文本内容创作                                         │
│                                                                           │
│  ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐      │
│  │                 │     │                 │     │                 │      │
│  │  内容规划       │────►│  分节生成       │────►│  递进整合        │      │
│  │                 │     │                 │     │                 │      │
│  └─────────────────┘     └─────────────────┘     └─────────────────┘      │
│         │                       │                       │                  │
│         ▼                       ▼                       ▼                  │
│  ┌─────────────┐         ┌─────────────┐         ┌─────────────┐          │
│  │             │         │             │         │             │          │
│  │ 大纲图式    │         │ 分节模板    │         │ 连贯性校验  │          │
│  │             │         │             │         │             │          │
│  └─────────────┘         └─────────────┘         └─────────────┘          │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```

### 实现：文档生成系统

```python
class LongFormGenerator:
    """用于生成连贯长文本内容的系统。"""
    
    def __init__(self, llm_service):
        self.llm = llm_service
        self.document_state = {
            "title": "",
            "outline": [],
            "sections": {},
            "current_section": "",
            "theme_keywords": [],
            "style_guide": {},
            "completed_sections": []
        }
    
    def create_outline(self, topic, length="medium", style="informative"):
        """为文档生成结构化大纲。"""
        outline_prompt = f"""
        任务：为关于{topic}的{length}篇{style}风格文档创建详细大纲。
        流程：
        1. 列出3-5个全面覆盖主题的主章节
        2. 每个主章节下列出2-4个子章节
        3. 每节附1-2句简要描述
        4. 给出章节间衔接建议
        格式：
        标题：[建议标题]
        主章节：
        1. [章节标题]
           - 描述：[简要描述]
           - 子章节：
             a. [子章节标题]
             b. [子章节标题]
           - 衔接：[衔接建议]
        2. [继续...]
        主题关键词：[5-7个关键词]
        风格建议：[3-4条]
        """
        outline_response = self.llm.generate(outline_prompt)
        self._parse_outline(outline_response)
        return self.document_state["outline"]
    
    def _parse_outline(self, outline_text):
        """解析大纲回复为结构化格式。"""
        # 实际实现应提取结构化大纲，这里用占位符
        self.document_state["title"] = "示例文档标题"
        self.document_state["outline"] = [
            {"title": "引言", "subsections": ["背景", "重要性"]},
            {"title": "主体一", "subsections": ["子主题A", "子主题B"]},
            {"title": "主体二", "subsections": ["子主题C", "子主题D"]},
            {"title": "结论", "subsections": ["总结", "未来展望"]}
        ]
        self.document_state["theme_keywords"] = ["关键词1", "关键词2", "关键词3"]
        self.document_state["style_guide"] = {
            "tone": "informative",
            "perspective": "third person",
            "style_notes": "多用具体例子"
        }
    
    def generate_section(self, section_index):
        """生成指定章节内容。"""
        section = self.document_state["outline"][section_index]
        self.document_state["current_section"] = section["title"]
        context = self._build_section_context(section_index)
        section_prompt = f"""
        任务：为题为“{self.document_state['title']}”的文档撰写“{section['title']}”章节。
        上下文：
        {context}
        指南：
        - 保持主题和前文一致
        - 覆盖所有子章节：{', '.join(section['subsections'])}
        - 保持{self.document_state['style_guide']['tone']}语气
        - 采用{self.document_state['style_guide']['perspective']}视角
        - {self.document_state['style_guide']['style_notes']}
        格式：
        ## {section['title']}
        [内容，约300-500字，涵盖所有子章节]
        """
        section_content = self.llm.generate(section_prompt)
        self.document_state["sections"][section["title"]] = section_content
        self.document_state["completed_sections"].append(section["title"])
        return section_content
    
    def _build_section_context(self, section_index):
        """为章节生成相关上下文。"""
        context = "前文摘要：\n"
        for title in self.document_state["completed_sections"]:
            content = self.document_state["sections"].get(title, "")
            summary = content[:100] + "..." if len(content) > 100 else content
            context += f"- {title}: {summary}\n"
        context += "\n主题关键词：" + ", ".join(self.document_state["theme_keywords"])
        total_sections = len(self.document_state["outline"])
        if section_index == 0:
            context += "\n这是文档的开篇章节。"
        elif section_index == total_sections - 1:
            context += "\n这是文档的结尾章节。"
        else:
            context += f"\n这是第{section_index + 1}节，共{total_sections}节。"
        return context
    
    def verify_coherence(self, section_index):
        """校验并提升章节间连贯性。"""
        if section_index == 0:
            return "首章无需连贯性校验。"
        section = self.document_state["outline"][section_index]
        previous_section = self.document_state["outline"][section_index - 1]
        current_content = self.document_state["sections"][section["title"]]
        previous_content = self.document_state["sections"][previous_section["title"]]
        coherence_prompt = f"""
        任务：校验并提升两相邻章节的连贯性。
        前一章：{previous_section['title']}
        {previous_content[-200:]}
        当前章：{section['title']}
        {current_content[:200]}
        流程：
        1. 识别主题或逻辑断裂
        2. 检查重复或矛盾
        3. 校验衔接是否流畅
        4. 术语和风格是否一致
        格式：
        连贯性评估：[良好/需改进]
        问题：
        1. [如有问题]
        2. [...]
        改进建议：
        [具体建议]
        """
        assessment = self.llm.generate(coherence_prompt)
        return assessment
    
    def generate_complete_document(self):
        """按章节顺序生成完整文档。"""
        if not self.document_state["outline"]:
            raise ValueError("请先生成大纲")
        all_content = [f"# {self.document_state['title']}\n\n"]
        for i in range(len(self.document_state["outline"])):
            section_content = self.generate_section(i)
            if i > 0:
                coherence_check = self.verify_coherence(i)
                # 实际应用中可用此结果优化章节
            all_content.append(section_content)
        return "\n\n".join(all_content)
```

该实现展示了：
1. **结构化内容规划**（提示程序）
2. **递进式上下文构建**（分节生成）
3. **章节连贯性校验**
4. **全程状态管理**

## 应用领域：带记忆的复杂推理

复杂推理常需跨多步跟踪状态并保留关键信息：

```
┌───────────────────────────────────────────────────────────────────────────┐
│                      复杂推理系统                                         │
│                                                                           │
│  ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐      │
│  │                 │     │                 │     │                 │      │
│  │  问题分析       │────►│  方案生成       │────►│  校验与优化      │      │
│  │                 │     │                 │     │                 │      │
│  └─────────────────┘     └─────────────────┘     └─────────────────┘      │
│         │                       │                       │                  │
│         ▼                       ▼                       ▼                  │
│  ┌─────────────┐         ┌─────────────┐         ┌─────────────┐          │
│  │             │         │             │         │             │          │
│  │ 结构化问题  │         │ 思维链模板  │         │ 自校正循环  │          │
│  │ 图式        │         │             │         │             │          │
│  └─────────────┘         └─────────────┘         └─────────────┘          │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```

### 实现：数学问题求解器

```python
class MathProblemSolver:
    """逐步解决复杂数学问题的系统。"""
    
    def __init__(self, llm_service):
        self.llm = llm_service
        self.problem_state = {
            "original_problem": "",
            "parsed_problem": {},
            "solution_steps": [],
            "current_step": 0,
            "verification_results": [],
            "final_answer": ""
        }
    
    def parse_problem(self, problem_text):
        """解析并结构化数学问题。"""
        parse_prompt = f"""
        任务：分析并结构化下列数学问题。
        问题：{problem_text}
        输出：
        1. 问题类型（如代数、几何等）
        2. 已知信息
        3. 需要解决的变量
        4. 相关公式或定理
        格式：
        问题类型：
        已知：
        1. [信息1]
        2. [信息2]
        待求：
        1. [变量1]
        2. [变量2]
        相关公式：
        - [公式1]
        - [公式2]
        """
        parsed_response = self.llm.generate(parse_prompt)
        self._parse_parsed_problem(parsed_response)
        return self.problem_state["parsed_problem"]
    
    def _parse_parsed_problem(self, parsed_text):
        """解析问题解析回复为结构化格式。"""
        # 实际实现应提取结构化问题信息，这里用占位符
        self.problem_state["original_problem"] = "示例问题：解方程2x+3=7"
        self.problem_state["parsed_problem"] = {
            "type": "代数",
            "given": ["2x+3=7"],
            "variables": ["x"],
            "formulas": ["方程平衡", "移项法"]
        }
    
    def generate_solution_steps(self):
        """生成解决问题的逐步方案。"""
        if not self.problem_state["parsed_problem"]:
            raise ValueError("请先解析问题")
        solution_prompt = f"""
        任务：为下列数学问题生成逐步解决方案。
        问题：{self.problem_state['original_problem']}
        已知：{', '.join(self.problem_state['parsed_problem']['given'])}
        待求：{', '.join(self.problem_state['parsed_problem']['variables'])}
        相关公式：{', '.join(self.problem_state['parsed_problem']['formulas'])}
        步骤：
        1. [第一步]
        2. [第二步]
        3. [第三步]
        ...
        格式：
        步骤1： [具体操作]
        步骤2： [具体操作]
        最终答案： [计算结果]
        """
        solution_response = self.llm.generate(solution_prompt)
        self.problem_state["solution_steps"] = self._parse_solution_steps(solution_response)
        return self.problem_state["solution_steps"]
    
    def _parse_solution_steps(self, solution_text):
        """解析解决方案回复为结构化步骤。"""
        # 实际实现应提取结构化步骤，这里用占位符
        return [
            "步骤1：将3从等式两边同时减去。",
            "步骤2：将等式两边同时除以2。",
            "最终答案：x = 2"
        ]
    
    def verify_solution(self):
        """校验解决方案的正确性。"""
        if not self.problem_state["solution_steps"]:
            raise ValueError("请先生成解决方案")
        verification_prompt = f"""
        任务：校验下列数学问题的解决方案。
        问题：{self.problem_state['original_problem']}
        步骤：
        {chr(10).join(self.problem_state['solution_steps'])}
        校验：
        1. 每一步是否正确应用了数学原理？
        2. 是否有逻辑漏洞或跳步？
        3. 最终答案是否正确？
        格式：
        校验结果：[通过/不通过]
        问题：
        1. [如有问题]
        2. [...]
        改进建议：
        [具体建议]
        """
        verification_response = self.llm.generate(verification_prompt)
        self.problem_state["verification_results"] = self._parse_verification_results(verification_response)
        return self.problem_state["verification_results"]
    
    def _parse_verification_results(self, verification_text):
        """解析校验结果回复为结构化格式。"""
        # 实际实现应提取结构化校验结果，这里用占位符
        return {
            "status": "通过",
            "issues": [],
            "suggestions": []
        }
```

该实现展示了：
1. **问题解析与结构化**
2. **基于模板的逐步推理**
3. **自我校验与优化建议**

## 结语

通过以上高级应用示例，我们可以看到，上下文工程的原理与方法如何在实际中助力于提升 LLM 的应用能力。从内容创作到复杂推理，结构化的上下文管理与智能化的步骤生成，展现了 AI 在各领域的广泛可能性。
