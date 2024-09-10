import os
import platform
import subprocess

def build_for_current_platform():
    system = platform.system().lower()
    if system == "windows":
        subprocess.run(["pyinstaller", "--onefile", "--windowed", "app.py"])
    elif system == "darwin":  # macOS
        subprocess.run(["pyinstaller", "--onefile", "--windowed", "app.py"])
    elif system == "linux":
        subprocess.run(["pyinstaller", "--onefile", "app.py"])
    else:
        print(f"Unsupported platform: {system}")

def build_for_all_platforms():
    # Windows
    subprocess.run(["pyinstaller", "--onefile", "--windowed", "-n", "ExamKiosk-Windows", "app.py"])
    
    # macOS
    subprocess.run(["pyinstaller", "--onefile", "--windowed", "-n", "ExamKiosk-Mac", "app.py"])
    
    # Linux
    subprocess.run(["pyinstaller", "--onefile", "-n", "ExamKiosk-Linux", "app.py"])

if __name__ == "__main__":
    choice = input("Build for current platform only? (y/n): ").lower()
    if choice == 'y':
        build_for_current_platform()
    else:
        build_for_all_platforms()

print("Build process completed. Check the 'dist' folder for the executable(s).")