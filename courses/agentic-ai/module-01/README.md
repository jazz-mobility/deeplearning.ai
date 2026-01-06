# Module 1: Introduction to Agentic Workflows

**Status**: Completed  
**Duration**: ~1 hour

## Overview

This module introduces the fundamentals of agentic AI systems - AI that can reason, plan, and take multi-step actions to achieve goals autonomously.

## Learning Objectives

- Understand what makes AI systems "agentic"
- Learn about different degrees of autonomy
- Explore task decomposition strategies
- Understand evaluation methods for agentic systems
- Identify real-world applications and use cases

---

## Key Concepts

### What is Agentic AI?

Agentic AI refers to systems that go beyond simple question-answering to:

1. **Take Actions**: Execute multi-step workflows autonomously
2. **Reason**: Think through problems step-by-step
3. **Plan**: Break down complex goals into sub-tasks
4. **Iterate**: Improve outputs through self-reflection
5. **Use Tools**: Leverage external APIs and capabilities

### Degrees of Autonomy

| Level | Description | Example |
|-------|-------------|---------|
| **Level 0** | No autonomy - direct prompting | ChatGPT basic Q&A |
| **Level 1** | Simple tool use | Calculator, web search |
| **Level 2** | Multi-step workflows | Research + summarize |
| **Level 3** | Self-directed planning | Autonomous coding agent |
| **Level 4** | Fully autonomous | Self-improving systems |

### Four Agentic Design Patterns

Andrew Ng identifies four key patterns for building agentic systems:

1. **Reflection**: Agent critiques and improves its own output
2. **Tool Use**: Agent calls external functions/APIs
3. **Planning**: Agent breaks down tasks and creates execution plans
4. **Multi-Agent**: Multiple specialized agents collaborate

### Task Decomposition

Breaking complex goals into manageable steps:

```
Goal: "Write a research report on quantum computing"
    ↓
Sub-tasks:
  1. Search for recent papers
  2. Identify key themes
  3. Write outline
  4. Draft each section
  5. Add citations
  6. Review and revise
```

---

## Lessons

| # | Lesson | Description |
|---|--------|-------------|
| 1 | Welcome | Course introduction |
| 2 | What is Agentic AI? | Core principles |
| 3 | Degrees of Autonomy | Spectrum of agent capabilities |
| 4 | Benefits and Applications | Real-world use cases |
| 5 | Task Decomposition | Breaking down complex goals |
| 6 | Agentic Design Patterns | Four key patterns |
| 7 | Evaluation Methods | Measuring agent performance |
| 8 | Quiz | Test your understanding |
| 9 | Optional Setup | Local environment guide |

---

## Learning Resources

### Official Documentation

- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
- [Anthropic Tool Use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
- [LangChain Agents](https://python.langchain.com/docs/modules/agents/)

### Research Papers

- [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629) - Yao et al., 2022
- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) - Wei et al., 2022
- [Toolformer](https://arxiv.org/abs/2302.04761) - Schick et al., 2023
- [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) - Significant Gravitas

### Blog Posts & Articles

- [Andrew Ng's Agentic AI Newsletter](https://www.deeplearning.ai/the-batch/)
- [Building LLM Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) - Lilian Weng
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)

### Videos

- [Andrew Ng: What's Next for AI Agents](https://www.youtube.com/watch?v=KrRD7r7y7NY)
- [AI Agents Explained](https://www.youtube.com/watch?v=F8NKVhkZZWI)

---

## Key Takeaways

1. **Agentic != Autonomous**: Agents can have varying degrees of autonomy
2. **Iteration is Key**: Multiple passes often beat single-shot generation
3. **Tools Extend Capabilities**: External APIs unlock real-world actions
4. **Decomposition Enables Complexity**: Break big problems into small steps
5. **Evaluation is Hard**: Need both automated metrics and human judgment

---

## Next Steps

Continue to [Module 2: Reflection Design Pattern](../module-02/README.md) to learn how agents can critique and improve their own outputs.
