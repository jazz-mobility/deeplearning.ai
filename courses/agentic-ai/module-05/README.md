# Module 5: Multi-Agent Workflows

**Status**: Completed  
**Duration**: ~1.5 hours  
**Lab**: `L3_Agentic_Workflows.ipynb`

## Overview

Learn how to build **multi-agent systems** where specialized agents collaborate to complete complex research tasks. This module combines planning, tool use, and reflection patterns into a cohesive agentic workflow.

## Learning Objectives

- Build a multi-agent orchestration system
- Implement specialized agents (Planner, Researcher, Writer, Editor)
- Coordinate agent execution through a central executor
- Combine tool use with reflection for high-quality outputs

---

## Key Concepts

### Multi-Agent Architecture

Instead of a single monolithic agent, this pattern uses specialized agents:

| Agent | Role | Capabilities |
|-------|------|--------------|
| **Planner** | Creates execution plan | Breaks topic into research steps |
| **Research Agent** | Gathers information | arXiv, Tavily, Wikipedia tools |
| **Writer Agent** | Drafts content | Academic/technical writing |
| **Editor Agent** | Reviews & improves | Reflection and critique |
| **Executor** | Orchestrates workflow | Routes tasks to appropriate agents |

### Workflow Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    MULTI-AGENT WORKFLOW                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. PLANNING                                                │
│     └── Planner Agent: Generate step-by-step research plan  │
│                                                             │
│  2. EXECUTION (for each step)                               │
│     ├── Executor: Decide which agent handles the step       │
│     ├── Research Agent: Search arXiv/Tavily/Wikipedia       │
│     ├── Writer Agent: Draft sections                        │
│     └── Editor Agent: Reflect and revise                    │
│                                                             │
│  3. OUTPUT                                                  │
│     └── Final Markdown research report                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Implementation

### Agent Registry Pattern

```python
agent_registry = {
    "research_agent": research_agent,
    "editor_agent": editor_agent,
    "writer_agent": writer_agent,
}
```

### Planner Agent

Generates a Python list of executable steps:

```python
def planner_agent(topic: str, model: str = "openai:o4-mini") -> list[str]:
    user_prompt = f"""
    You are a planning agent responsible for organizing a research workflow.

    Available agents:
    - A research agent who can search the web, Wikipedia, and arXiv.
    - A writer agent who can draft research summaries.
    - An editor agent who can reflect and revise the drafts.

    Write a step-by-step research plan as a valid Python list.
    Each step should be atomic and executable.

    Topic: "{topic}"
    """
    
    response = CLIENT.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": user_prompt}],
        temperature=1,
    )
    
    steps_str = response.choices[0].message.content.strip()
    return ast.literal_eval(steps_str)
```

### Research Agent (with Tools)

```python
def research_agent(task: str, model: str = "openai:gpt-4o"):
    prompt = f"""
    You are a research assistant with access to:
    - arxiv_tool: Academic papers
    - tavily_tool: Web searches
    - wikipedia_tool: Encyclopedic knowledge

    Current date: {datetime.now().strftime('%Y-%m-%d')}
    Your task: {task}
    """
    
    tools = [
        research_tools.arxiv_search_tool,
        research_tools.tavily_search_tool,
        research_tools.wikipedia_search_tool
    ]
    
    response = CLIENT.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        tools=tools,
        tool_choice="auto",
        max_turns=6
    )
    
    return response.choices[0].message.content
```

### Writer & Editor Agents

```python
def writer_agent(task: str, model: str = "openai:gpt-4o") -> str:
    system_prompt = "You are a writing agent specialized in academic/technical content."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": task}
    ]
    response = CLIENT.chat.completions.create(model=model, messages=messages, temperature=1.0)
    return response.choices[0].message.content

def editor_agent(task: str, model: str = "openai:gpt-4o") -> str:
    system_prompt = "You are an editor agent specialized in reflecting on and improving drafts."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": task}
    ]
    response = CLIENT.chat.completions.create(model=model, messages=messages, temperature=0.7)
    return response.choices[0].message.content
```

### Executor Agent (Orchestrator)

The executor routes each plan step to the appropriate agent:

```python
def executor_agent(topic, model: str = "openai:gpt-4o"):
    plan_steps = planner_agent(topic)
    history = []

    for step in plan_steps:
        # LLM decides which agent handles this step
        agent_decision_prompt = f"""
        Given this instruction, identify which agent should perform it.
        Return JSON: {{"agent": "...", "task": "..."}}
        Instruction: "{step}"
        """
        
        response = CLIENT.chat.completions.create(...)
        agent_info = json.loads(response.choices[0].message.content)
        
        # Build context from previous steps
        context = "\n".join([f"Step {j+1}: {r}" for j, (_, _, r) in enumerate(history)])
        enriched_task = f"Context:\n{context}\n\nTask: {agent_info['task']}"
        
        # Execute with selected agent
        output = agent_registry[agent_info["agent"]](enriched_task)
        history.append((step, agent_info["agent"], output))

    return history
```

---

## Lab Exercises

1. **Exercise 1**: `planner_agent(topic)` - Generate research plan as Python list
2. **Exercise 2**: `research_agent(task)` - Execute research with tool calling
3. **Exercise 3**: `writer_agent(task)` - Draft academic content
4. **Exercise 4**: `editor_agent(task)` - Reflect and improve drafts

### Running the Lab

```bash
mise run m5
```

**Required Environment Variables:**
```toml
# .mise.local.toml
[env]
OPENAI_API_KEY = "sk-..."
TAVILY_API_KEY = "tvly-..."
```

---

## Design Patterns Combined

This module combines all previous patterns:

| Pattern | How It's Used |
|---------|---------------|
| **Planning** | Planner agent decomposes topic into steps |
| **Tool Use** | Research agent uses arXiv, Tavily, Wikipedia |
| **Reflection** | Editor agent critiques and improves drafts |
| **Multi-Agent** | Specialized agents with executor orchestration |

---

## Key Takeaways

1. **Specialization**: Different agents excel at different tasks
2. **Orchestration**: Central executor routes work to appropriate agents
3. **Context Passing**: Each step builds on previous outputs
4. **Dynamic Routing**: LLM decides which agent handles each step
5. **Combined Patterns**: Planning + Tool Use + Reflection = Powerful workflows

---

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Plan steps too vague | Be specific about agent capabilities in planner prompt |
| Lost context between steps | Pass history/context to each agent |
| Wrong agent selection | Clear agent descriptions in routing prompt |
| Too many steps | Limit max steps to manage execution time |

---

## Learning Resources

### Documentation

- [aisuite Library](https://github.com/andrewyng/aisuite) - Multi-provider LLM client
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)

### Research Papers

- [AutoGen: Multi-Agent Conversations](https://arxiv.org/abs/2308.08155) - Microsoft, 2023
- [CAMEL: Communicative Agents](https://arxiv.org/abs/2303.17760) - Li et al., 2023
- [MetaGPT: Multi-Agent Framework](https://arxiv.org/abs/2308.00352) - Hong et al., 2023

---

## Dependencies

Key libraries used:
- `openai` - OpenAI API
- `aisuite` - Multi-LLM abstraction with tool support
- `tavily-python` - Web search API
- `jupyter` - Interactive notebooks
