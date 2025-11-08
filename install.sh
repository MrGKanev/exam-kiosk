#!/bin/bash

# Exam Kiosk Installation Script
# Requires Python 3.8+ (Python 3.11+ recommended)

set -e  # Exit on error

echo "Starting Exam Kiosk installation..."

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
REQUIRED_VERSION="3.8"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "Error: Python $REQUIRED_VERSION or higher is required. Found Python $PYTHON_VERSION"
    exit 1
fi

echo "Python version $PYTHON_VERSION detected - OK"

# Update package list
echo "Updating package list..."
sudo apt-get update

# Install Python3 and pip if not already installed
echo "Installing Python3 and pip..."
sudo apt-get install -y python3 python3-pip

# Install system dependencies for PyQt5
echo "Installing system dependencies..."
sudo apt-get install -y libqt5webkit5-dev build-essential python3-dev libssl-dev libffi-dev

# Upgrade pip
echo "Upgrading pip..."
pip3 install --upgrade pip

# Install Python packages from requirements.txt
echo "Installing Python dependencies from requirements.txt..."
pip3 install -r requirements.txt

echo ""
echo "Installation completed successfully!"
echo "You can now run the Exam Kiosk application with: python3 app.py"
echo "Or create executables with: python3 build.py"