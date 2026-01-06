# DeepLearning.AI Courses

This monorepo contains coursework, labs, and projects from various DeepLearning.AI courses.

## Structure

```
agentic-ai/
├── courses/              # Individual courses
│   └── agentic-ai/      # Agentic AI course
│       ├── module-01/   # Introduction to Agentic Workflows
│       ├── module-02/   # Reflection Design Pattern
│       └── module-03/   # Tool Use Design Pattern
├── shared/              # Shared utilities across courses
│   └── common/         # Common helper functions
└── scripts/            # Setup and utility scripts
```

## Setup

This project uses [mise](https://mise.jdx.dev/) for tool management and [uv](https://docs.astral.sh/uv/) for Python package management.

### Prerequisites

- [mise](https://mise.jdx.dev/getting-started.html) installed
- Git

### Quick Start

```bash
# Clone the repository
git clone <your-repo-url>
cd agentic-ai

# Run setup script
./scripts/setup.sh

# Activate the environment
mise activate
```

### Manual Setup

```bash
# Install tools (Python 3.11, uv, Node.js 18)
mise install

# Sync dependencies
uv sync

# Activate environment
eval "$(mise activate bash)"  # or zsh, fish, etc.
```

## Courses

### Agentic AI

**Status**: In Progress

Learn about agentic AI systems with iterative, multi-step workflows.

- [Course Link](https://learn.deeplearning.ai/courses/agentic-ai)
- [Course README](courses/agentic-ai/README.md)

#### Modules

| Module | Topic | Status |
|--------|-------|--------|
| 01 | Introduction to Agentic Workflows | Completed |
| 02 | Reflection Design Pattern | Completed |
| 03 | Tool Use Design Pattern | Completed |

#### Running Labs

```bash
mise run install   # Install dependencies
mise run m2        # Module 2 - Reflection lab
mise run m3        # Module 3 - Tool Use lab
mise run lab       # Open Jupyter browser
```

## Development

### Adding a New Course

```bash
# Create course structure
mkdir -p courses/new-course/module-01/{helpers,data}

# Create course pyproject.toml
cat > courses/new-course/pyproject.toml <<EOF
[project]
name = "new-course"
version = "0.1.0"
description = "Course description"
requires-python = ">=3.10"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
EOF

# Sync dependencies
uv sync
```

### Adding a New Module

```bash
# Create module structure
mkdir -p courses/agentic-ai/module-02/{helpers,data}

# Module dependencies are inherited from course-level pyproject.toml
```

### Working with Jupyter Notebooks

```bash
# Start Jupyter via mise
mise run lab

# Or directly
uv run jupyter notebook
```

### Environment Variables

Create `.mise.local.toml` (gitignored) for API keys:

```toml
[env]
OPENAI_API_KEY = "your-key"
TAVILY_API_KEY = "your-key"
```

## Tools

- **mise**: Tool version management (Python, Node.js, uv)
- **uv**: Fast Python package manager and workspace manager
- **Python 3.11**: Primary Python version
- **Jupyter**: For running course notebooks

## License

This repository contains course materials and personal coursework. Please refer to DeepLearning.AI's terms of service for usage restrictions.
