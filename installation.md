# Installation Guide

## Prerequisites

### Python Version

AOW requires Python 3.8 or higher. Check your Python version:

```bash
python --version
# or
python3 --version

System Requirements

    Memory: At least 4GB RAM (8GB recommended for large parameters)

    Storage: 1GB free disk space

    Processor: 64-bit architecture

Installation Methods
Method 1: Install from Source

    Clone the repository:
    bash

git clone https://github.com/KryptoResearcher/AOW.git
cd AOW

Install in development mode:
bash

pip install -e .

Method 2: Install with Optional Dependencies

For benchmarking and visualization:
bash

pip install -e .[benchmarks]

Method 3: Install for Development

For contributing to the project:
bash

pip install -e .[dev]

Verification

Verify the installation by running a simple test:
bash

python -c "from src.core.fields import FiniteField; print('Installation successful')"

Docker Installation

Alternatively, use Docker for a containerized environment:

    Build the Docker image:
    bash

docker build -t aow .

Run a container:
bash

docker run -it aow python examples/basic_iteration.py

Troubleshooting
Common Issues

    Permission Errors
    bash

# Use virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
pip install -e .

Missing Dependencies
bash

# Update pip
pip install --upgrade pip
# Reinstall
pip install -e .

Platform-Specific Issues

Windows: Ensure you have the latest C++ build tools

macOS: Install Xcode command line tools:
bash

xcode-select --install

Linux: Install Python development packages:
bash

# Ubuntu/Debian
sudo apt-get install python3-dev
# CentOS/RHEL
sudo yum install python3-devel

Uninstallation

To uninstall AOW:
bash

pip uninstall aow

Getting Help

If you encounter installation issues:

    Check the FAQ

    Review the troubleshooting section

    Open an issue on GitHub with:

        Your operating system

        Python version

        Complete error message