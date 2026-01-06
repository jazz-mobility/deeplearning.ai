# Module 3: Tool Use Design Pattern

**Status**: Completed  
**Duration**: ~1.5 hours  
**Lab**: `m3_graded_lab_tool_use_reflective_agents.ipynb`

## Overview

Learn how to build agents that can **call external tools** - APIs, databases, search engines, and custom functions. This pattern enables LLMs to access real-time information and perform actions in the real world.

## Learning Objectives

- Understand OpenAI's function calling API
- Define tools with JSON schemas
- Implement a tool-calling loop
- Combine tool use with reflection
- Build a complete research pipeline

---

## Key Concepts

### Why Tool Use?

LLMs have fundamental limitations that tools overcome:

| Limitation | Tool Solution |
|------------|---------------|
| Knowledge cutoff | Web search, APIs |
| No real-time data | Live data feeds |
| Can't perform calculations reliably | Calculator tools |
| Can't access private data | Database queries |
| Can't take actions | API integrations |

### How Tool Calling Works

```
┌──────────────┐
│  User Query  │
└──────┬───────┘
       │
       ▼
┌──────────────────────────────────────┐
│            LLM DECIDES               │
│  "I need to search for information"  │
│                                      │
│  Returns: tool_call with arguments   │
└──────┬───────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────┐
│         YOUR CODE EXECUTES           │
│    tool_function(**arguments)        │
│                                      │
│    Returns: result data              │
└──────┬───────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────┐
│         LLM CONTINUES                │
│  Uses tool results to answer query   │
│                                      │
│  Returns: final response             │
└──────────────────────────────────────┘
```

### Tool Definition Schema

Tools are defined using JSON Schema:

```python
tool_definition = {
    "type": "function",
    "function": {
        "name": "search_arxiv",                    # Function name
        "description": "Search academic papers",   # When to use
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query"
                },
                "max_results": {
                    "type": "integer",
                    "description": "Max papers to return",
                    "default": 5
                }
            },
            "required": ["query"]                  # Required params
        }
    }
}
```

---

## Implementation

### Basic Tool Calling Loop

```python
from openai import OpenAI
import json

client = OpenAI()

TOOL_MAPPING = {
    "search_web": search_web_function,
    "search_arxiv": search_arxiv_function,
}

def agent_with_tools(prompt: str, tools: list, max_turns: int = 10) -> str:
    messages = [
        {"role": "system", "content": "You are a helpful research assistant."},
        {"role": "user", "content": prompt}
    ]
    
    for _ in range(max_turns):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=tools,
            tool_choice="auto"  # Let model decide when to use tools
        )
        
        msg = response.choices[0].message
        messages.append(msg)
        
        # If no tool calls, we have the final answer
        if not msg.tool_calls:
            return msg.content
        
        # Execute each tool call
        for call in msg.tool_calls:
            tool_name = call.function.name
            args = json.loads(call.function.arguments)
            
            # Call the actual function
            result = TOOL_MAPPING[tool_name](**args)
            
            # Add result to messages
            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "name": tool_name,
                "content": json.dumps(result)
            })
    
    return messages[-1].content
```

### Tool Choice Options

```python
# Let model decide (recommended)
tool_choice="auto"

# Force model to use a specific tool
tool_choice={"type": "function", "function": {"name": "search_arxiv"}}

# Force model to use some tool (any tool)
tool_choice="required"

# Prevent tool use
tool_choice="none"
```

### Implementing Tools

#### arXiv Search Tool

```python
import urllib.request
import xml.etree.ElementTree as ET

def arxiv_search_tool(query: str, max_results: int = 5) -> list[dict]:
    base_url = "http://export.arxiv.org/api/query"
    params = f"search_query=all:{query}&max_results={max_results}"
    
    with urllib.request.urlopen(f"{base_url}?{params}") as response:
        data = response.read().decode("utf-8")
    
    root = ET.fromstring(data)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    
    results = []
    for entry in root.findall("atom:entry", ns):
        results.append({
            "title": entry.find("atom:title", ns).text,
            "summary": entry.find("atom:summary", ns).text,
            "url": entry.find("atom:id", ns).text
        })
    
    return results
```

#### Tavily Web Search Tool

```python
from tavily import TavilyClient

def tavily_search_tool(query: str, max_results: int = 5) -> list[dict]:
    client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
    response = client.search(query=query, max_results=max_results)
    
    return [
        {"title": r["title"], "content": r["content"], "url": r["url"]}
        for r in response["results"]
    ]
```

---

## Research Pipeline

The lab builds a complete pipeline combining tools and reflection:

```
┌─────────────────────────────────────────────┐
│              RESEARCH PIPELINE              │
├─────────────────────────────────────────────┤
│                                             │
│  1. SEARCH (Tool Use)                       │
│     ├── arXiv: Academic papers              │
│     └── Tavily: Web sources                 │
│                                             │
│  2. GENERATE                                │
│     └── Create report with citations        │
│                                             │
│  3. REFLECT                                 │
│     └── Critique: strengths, weaknesses     │
│                                             │
│  4. REVISE                                  │
│     └── Improve based on reflection         │
│                                             │
│  5. FORMAT                                  │
│     └── Convert to styled HTML              │
│                                             │
└─────────────────────────────────────────────┘
```

---

## Lab Exercises

1. **Exercise 1**: `generate_research_report_with_tools(prompt)`
   - Implement tool calling loop
   - Handle tool results
   - Generate cited report

2. **Exercise 2**: `reflection_and_rewrite(report)`
   - Structured reflection (JSON output)
   - Strengths, limitations, suggestions

3. **Exercise 3**: `convert_report_to_html(report)`
   - Transform plaintext to HTML
   - Preserve citations and links

### Running the Lab

```bash
mise run m3
```

**Required Environment Variables:**
```toml
# .mise.local.toml
[env]
OPENAI_API_KEY = "sk-..."
TAVILY_API_KEY = "tvly-..."
```

---

## Learning Resources

### Official Documentation

- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
- [OpenAI Tools Guide](https://platform.openai.com/docs/assistants/tools)
- [Anthropic Tool Use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
- [Tavily API](https://docs.tavily.com/)
- [arXiv API](https://info.arxiv.org/help/api/index.html)

### Research Papers

- [Toolformer: LMs Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) - Schick et al., 2023
- [MRKL Systems](https://arxiv.org/abs/2205.00445) - Karpas et al., 2022
- [ReAct: Reasoning and Acting](https://arxiv.org/abs/2210.03629) - Yao et al., 2022
- [WebGPT](https://arxiv.org/abs/2112.09332) - OpenAI, 2021

### Tutorials & Guides

- [OpenAI Cookbook: Function Calling](https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models)
- [Building a Research Assistant](https://python.langchain.com/docs/tutorials/agents/)

---

## Key Takeaways

1. **Tools = Real-World Capabilities**: Access live data, perform actions
2. **JSON Schema Definitions**: Clear structure for tool parameters
3. **Loop Until Done**: Keep calling tools until model is satisfied
4. **tool_choice="auto"**: Let model decide when tools are needed
5. **Combine Patterns**: Tool use + reflection = powerful pipelines

---

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Forgetting `tool_call_id` | Must match call ID in tool response |
| Not JSON-serializing results | Always `json.dumps()` tool output |
| Infinite loops | Set `max_turns` limit |
| Vague tool descriptions | Be specific about when to use each tool |
| Missing error handling | Wrap tool calls in try/except |

---

## Tool Definition Best Practices

1. **Clear Names**: `search_arxiv` not `tool1`
2. **Detailed Descriptions**: When and why to use the tool
3. **Parameter Descriptions**: What each argument does
4. **Sensible Defaults**: Reduce required parameters
5. **Type Hints**: Help model format arguments correctly

---

## Next Steps

Continue to **Module 4: Planning Design Pattern** to learn how agents can break down complex tasks and create execution plans.
