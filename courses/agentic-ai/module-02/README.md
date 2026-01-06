# Module 2: Reflection Design Pattern

**Status**: Completed  
**Duration**: ~1.5 hours  
**Lab**: `m2_graded_lab_reflection_research_agent.ipynb`

## Overview

Learn how to implement the **Reflection Pattern** - where an LLM critiques and improves its own output through iterative refinement. This is one of the most powerful techniques for improving AI output quality.

## Learning Objectives

- Understand why reflection improves output quality
- Implement a three-step draft → reflect → revise workflow
- Use different models for generation vs. reflection
- Evaluate the impact of reflection on output quality

---

## Key Concepts

### Why Reflection Works

LLMs are often better at **evaluating** content than **generating** it perfectly on the first try:

1. **Separation of Concerns**: Generation and evaluation are different cognitive tasks
2. **Fresh Perspective**: Reviewing with "fresh eyes" catches issues
3. **Explicit Criteria**: Reflection prompts can specify quality dimensions
4. **Iterative Refinement**: Multiple passes compound improvements

### The Reflection Workflow

```
┌─────────────────┐
│   User Input    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  1. GENERATE    │  ← First LLM call: Create initial draft
│     Draft       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  2. REFLECT     │  ← Second LLM call: Critique the draft
│    Feedback     │     (Can use different/stronger model)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  3. REVISE      │  ← Third LLM call: Improve based on feedback
│  Final Output   │
└─────────────────┘
```

### When to Use Reflection

| Use Case | Why It Helps |
|----------|--------------|
| **Writing tasks** | Catches structural issues, improves flow |
| **Code generation** | Finds bugs, improves readability |
| **Analysis** | Identifies gaps, strengthens arguments |
| **Creative work** | Refines style, adds depth |

---

## Implementation

### Basic Pattern

```python
def generate_draft(topic: str, model: str = "gpt-4o") -> str:
    prompt = f"""Write a complete essay on: {topic}
    
    Include:
    - Introduction with thesis
    - Body paragraphs with evidence
    - Conclusion summarizing main points"""
    
    return llm_call(prompt, model=model)


def reflect_on_draft(draft: str, model: str = "gpt-4o") -> str:
    prompt = f"""Analyze this essay and provide constructive feedback:

    {draft}

    Address:
    - Structure and organization
    - Clarity of arguments
    - Evidence and reasoning
    - Writing style and flow
    - Specific areas for improvement
    
    Be critical but constructive."""
    
    return llm_call(prompt, model=model)


def revise_draft(draft: str, feedback: str, model: str = "gpt-4o") -> str:
    prompt = f"""Revise this essay based on the feedback provided.

    Original Essay:
    {draft}

    Feedback:
    {feedback}

    Create an improved version addressing all feedback points.
    Return only the revised essay."""
    
    return llm_call(prompt, model=model)
```

### Using Different Models

A powerful technique is using different models for different steps:

```python
# Faster/cheaper model for initial draft
draft = generate_draft(topic, model="gpt-4o-mini")

# Stronger reasoning model for reflection
feedback = reflect_on_draft(draft, model="o1-mini")

# Back to standard model for revision
final = revise_draft(draft, feedback, model="gpt-4o")
```

### Multiple Reflection Rounds

```python
def iterative_reflection(topic: str, rounds: int = 2) -> str:
    draft = generate_draft(topic)
    
    for i in range(rounds):
        feedback = reflect_on_draft(draft)
        draft = revise_draft(draft, feedback)
        print(f"Round {i+1} complete")
    
    return draft
```

---

## Lab Exercise

The graded lab implements a **Research Agent** with reflection:

1. **Exercise 1**: `generate_draft(topic)` - Create initial essay
2. **Exercise 2**: `reflect_on_draft(draft)` - Critique the essay
3. **Exercise 3**: `revise_draft(draft, feedback)` - Improve based on feedback

### Running the Lab

```bash
mise run m2
```

---

## Learning Resources

### Research Papers

- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) - Madaan et al., 2023
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) - Shinn et al., 2023
- [Constitutional AI](https://arxiv.org/abs/2212.08073) - Anthropic, 2022
- [Self-Consistency Improves Chain of Thought](https://arxiv.org/abs/2203.11171) - Wang et al., 2022

### Documentation

- [OpenAI Chat Completions](https://platform.openai.com/docs/guides/chat-completions)
- [aisuite Library](https://github.com/andrewyng/aisuite) - Multi-provider LLM client

### Blog Posts

- [Self-Reflection in LLMs](https://www.promptingguide.ai/techniques/reflexion)
- [Improving LLM Outputs with Self-Critique](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/)

---

## Key Takeaways

1. **Reflection > Single Pass**: Even simple reflection improves quality significantly
2. **Separate Generation from Evaluation**: Different prompts for different tasks
3. **Use Stronger Models for Reflection**: Reasoning models excel at critique
4. **Iterate When Needed**: Multiple rounds can help for complex tasks
5. **Be Specific in Feedback Prompts**: List exact criteria to evaluate

---

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Vague reflection prompts | Specify exact quality dimensions |
| Too many iterations | 1-2 rounds usually sufficient |
| Same model for everything | Consider stronger model for reflection |
| Not using feedback | Ensure revision prompt includes all feedback |

---

## Next Steps

Continue to [Module 3: Tool Use Design Pattern](../module-03/README.md) to learn how agents can call external tools and APIs.
