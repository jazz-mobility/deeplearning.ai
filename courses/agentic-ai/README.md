# Agentic AI Course

**Instructor**: Andrew Ng  
**Platform**: [DeepLearning.AI](https://learn.deeplearning.ai/courses/agentic-ai)  
**Level**: Intermediate  
**Duration**: ~6 hours

## Course Overview

Learn to build agentic AI systems with iterative, multi-step workflows that can reason, plan, and take action to achieve complex goals.

## Quick Start

```bash
mise run install   # Install dependencies
mise run m2        # Open Module 2 lab
mise run m3        # Open Module 3 lab
mise run m5        # Open Module 5 lab
```

---

## Module 1: Introduction to Agentic Workflows

### Key Concepts

- **Agentic AI**: Systems that can iterate, reason, and improve their outputs autonomously
- **Degrees of Autonomy**: Spectrum from simple prompting to fully autonomous agents
- **Task Decomposition**: Breaking complex goals into manageable sub-tasks

### Learning Notes

1. **What makes AI "agentic"?**
   - Ability to take actions in multi-step workflows
   - Self-reflection and iterative improvement
   - Tool use and external system interaction
   - Planning and reasoning capabilities

2. **Benefits of Agentic Workflows**
   - Better quality outputs through iteration
   - Handling of complex, multi-step tasks
   - Reduced need for human intervention
   - More reliable and consistent results

---

## Module 2: Reflection Design Pattern

**Lab**: `m2_graded_lab_reflection_research_agent.ipynb`

### Key Concepts

- **Reflection Pattern**: LLM critiques and improves its own output
- **Draft → Reflect → Revise**: Three-step workflow for quality improvement
- **Self-Critique**: Using reasoning to identify weaknesses

### Learning Notes

1. **Why Reflection Works**
   - LLMs can identify issues they couldn't avoid in first pass
   - Separation of generation and evaluation tasks
   - Mimics human writing/editing process

2. **Three-Step Workflow**
   ```
   Step 1: Generate initial draft
   Step 2: Reflect/critique the draft (identify issues)
   Step 3: Revise based on feedback
   ```

3. **Implementation Pattern**
   ```python
   def generate_draft(topic):
       # First LLM call - generate content
       prompt = f"Write an essay on: {topic}"
       return llm_call(prompt)
   
   def reflect_on_draft(draft):
       # Second LLM call - critique (can use different model)
       prompt = f"Provide constructive feedback on:\n{draft}"
       return llm_call(prompt)
   
   def revise_draft(draft, feedback):
       # Third LLM call - improve based on feedback
       prompt = f"Revise this draft based on feedback:\n{draft}\n\nFeedback:\n{feedback}"
       return llm_call(prompt)
   ```

4. **Key Insights**
   - Different models can be used for different steps (e.g., stronger model for reflection)
   - Can iterate multiple rounds of reflect/revise
   - Quality improves significantly with reflection vs. single-pass generation

---

## Module 3: Tool Use Design Pattern

**Lab**: `m3_graded_lab_tool_use_reflective_agents.ipynb`

### Key Concepts

- **Tool Calling**: LLMs invoking external functions/APIs
- **Research Pipeline**: Search → Reflect → Format workflow
- **OpenAI Function Calling**: Structured tool definitions and responses

### Learning Notes

1. **Why Tool Use?**
   - LLMs have knowledge cutoffs
   - Need real-time data (web search, APIs)
   - Access to specialized capabilities (calculators, databases)
   - Grounding responses in facts

2. **Tool Definition Structure**
   ```python
   tool_def = {
       "type": "function",
       "function": {
           "name": "search_arxiv",
           "description": "Search academic papers on arXiv",
           "parameters": {
               "type": "object",
               "properties": {
                   "query": {"type": "string", "description": "Search query"},
                   "max_results": {"type": "integer", "default": 5}
               },
               "required": ["query"]
           }
       }
   }
   ```

3. **Tool Calling Loop**
   ```python
   while True:
       response = client.chat.completions.create(
           model="gpt-4o",
           messages=messages,
           tools=tools,
           tool_choice="auto"  # Let model decide
       )
       
       msg = response.choices[0].message
       
       # If no tool calls, we have final answer
       if not msg.tool_calls:
           return msg.content
       
       # Execute each tool call
       for call in msg.tool_calls:
           result = execute_tool(call.function.name, call.function.arguments)
           messages.append({
               "role": "tool",
               "tool_call_id": call.id,
               "content": json.dumps(result)
           })
   ```

4. **Research Agent Pipeline**
   ```
   User Query
       ↓
   [Tool: arXiv Search] → Academic papers
   [Tool: Tavily Search] → Web results
       ↓
   Generate Report (with citations)
       ↓
   Reflect & Revise
       ↓
   Convert to HTML
   ```

5. **Key Insights**
   - `tool_choice="auto"` lets model decide when to use tools
   - Tool results go back as `role: "tool"` messages
   - Combine with reflection for higher quality outputs
   - Always include `tool_call_id` to link results to calls

---

## Design Patterns Summary

| Pattern | When to Use | Key Benefit |
|---------|-------------|-------------|
| **Reflection** | Quality-critical content generation | Iterative improvement |
| **Tool Use** | Need external data/capabilities | Real-time, grounded responses |
| **Combined** | Research, reports, analysis | Best of both worlds |

---

## Dependencies

Key libraries used:
- `openai` - OpenAI API (GPT-4o, tool calling)
- `aisuite` - Multi-LLM abstraction
- `tavily-python` - Web search API
- `jupyter` - Interactive notebooks

## Environment Variables

Required in `.mise.local.toml`:
```toml
[env]
OPENAI_API_KEY = "sk-..."
TAVILY_API_KEY = "tvly-..."
```

---

## Progress

- [x] Module 1: Introduction to Agentic Workflows
- [x] Module 2: Reflection Design Pattern
- [x] Module 3: Tool Use Design Pattern
- [x] Module 5: Multi-Agent Workflows (Agentic Workflows)
- [ ] Course Completion
