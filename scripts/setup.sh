#!/bin/bash
set -euo pipefail
echo "Setting up CRM Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
