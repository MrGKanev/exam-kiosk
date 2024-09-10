# Exam Kiosk

Exam Kiosk is a simple, secure kiosk application designed for exam environments. It creates a fullscreen browser window that prevents users from accessing other applications or exiting the exam environment.

## Features

- Fullscreen kiosk mode
- Blocks common keyboard shortcuts to prevent exiting
- Loads a specified URL (currently set to <https://gkanev.com>)
- Secret exit combination (Ctrl+Alt+Q) for authorized personnel

## Requirements

- Python 3.6+
- PyQt5
- PyQtWebEngine
- pynput
- PyInstaller (for creating executables)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/MrGKanev/exam-kiosk.git
   cd exam-kiosk
   ```

2. Run the installation script:

   ```
   bash install.sh
   ```

   This script will install all necessary dependencies, including PyInstaller.

## Usage

To start the Exam Kiosk application, run:

```
python3 app.py
```

The application will start in fullscreen mode, loading the specified URL.

To exit the application, use the secret key combination: Ctrl+Alt+Q

## Building Executables

To create standalone executables for Windows, macOS, and Linux:

1. Ensure you have run the `install.sh` script to install PyInstaller.
2. Run the build script:

   ```
   python3 build.py
   ```

3. Choose whether to build for the current platform only or for all platforms.
4. The executables will be created in the `dist` folder.

Note: Cross-platform building may not always work perfectly. For best results, build on each target platform separately.

## Customization

To change the URL loaded by the kiosk, modify the following line in `app.py`:

```python
self.browser.setUrl(QUrl("https://gkanev.com"))
```

Replace `"https://gkanev.com"` with your desired URL.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For any questions or concerns, please open an issue on the GitHub repository.
