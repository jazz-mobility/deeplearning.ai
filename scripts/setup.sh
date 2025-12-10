#!/bin/bash

# Setup script for Agentic AI course monorepo

set -e

echo "Setting up development environment..."

# Install tools via mise
echo "Installing tools with mise..."
mise install

# Sync dependencies with uv
echo "Syncing dependencies with uv..."
uv sync

echo "Setup complete!"
echo "To activate the environment, run: mise activate"
echo "Or use: eval \"\$(mise activate bash)\" for bash, or equivalent for your shell."