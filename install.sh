#!/bin/bash

# Update package list
sudo apt-get update

# Install Python3 and pip if not already installed
sudo apt-get install -y python3 python3-pip

# Install required Python packages
pip3 install PyQt5 PyQtWebEngine pynput pyinstaller

# Install system dependencies for PyQt5
sudo apt-get install -y libqt5webkit5-dev build-essential python3-dev libssl-dev libffi-dev

echo "Installation completed. You can now run the Exam Kiosk application or create executables."