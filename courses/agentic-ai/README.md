# Agentic AI Course

**Instructor**: Andrew Ng
**Platform**: [DeepLearning.AI](https://learn.deeplearning.ai/courses/agentic-ai)
**Level**: Intermediate
**Duration**: ~5 hours 54 minutes
**Status**: In Progress (Module 1 ✅)

## Course Overview

Learn to build agentic AI systems with iterative, multi-step workflows that can reason, plan, and take action to achieve complex goals.

## What You'll Learn

- Understanding agentic AI and degrees of autonomy
- Task decomposition and planning strategies
- Agentic design patterns and workflows
- Building multi-step reasoning systems
- Evaluation methods for agentic systems
- Real-world applications and use cases

## Modules

### ✅ Module 1: Introduction to Agentic Workflows
- [Lesson 1: Welcome](module-01/)
- Understanding what makes AI "agentic"
- Degrees of autonomy in AI systems
- Benefits and applications of agentic workflows
- Task decomposition techniques
- Evaluation frameworks

**Status**: Completed

### 🔄 Module 2: Coming Soon
**Status**: Not Started

## Getting Started

### Setup Environment

From the repository root:
```bash
./scripts/setup.sh
mise activate
```

### Start Jupyter

```bash
cd courses/agentic-ai/module-01
jupyter notebook
```

## Module Structure

Each module contains:
- `lesson-*.ipynb` - Jupyter notebooks for hands-on labs
- `helpers/` - Helper scripts and utilities
- `data/` - Sample data for exercises
- `pyproject.toml` - Module-specific dependencies

## Course Resources

- [Course Homepage](https://learn.deeplearning.ai/courses/agentic-ai)
- [Environment Setup Guide](https://learn.deeplearning.ai/courses/agentic-ai/lesson/bvuwky83/optional%3A-set-up-your-local-environment-for-the-ungraded-labs)

## Notes & Learnings

### Module 1: Key Takeaways
- Agentic AI systems can iterate and improve their outputs
- Task decomposition is crucial for complex goals
- Multiple design patterns exist for different use cases
- Evaluation requires both automated and human assessment

## Dependencies

See [pyproject.toml](pyproject.toml) for full dependency list.

Key libraries:
- `anthropic` - Claude API
- `openai` - OpenAI API
- `aisuite` - Multi-LLM framework
- `tavily-python` - Web search capabilities
- `fastapi` - API development
- `jupyter` - Interactive notebooks

## Progress Tracking

- [x] Module 1: Introduction to Agentic Workflows
- [ ] Module 2: TBD
- [ ] Module 3: TBD
- [ ] Course Completion

---

**Last Updated**: 2025-12-10
