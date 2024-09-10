# Exam Kiosk

Exam Kiosk is a simple, secure kiosk application designed for exam environments. It creates a fullscreen browser window that prevents users from accessing other applications or exiting the exam environment.

## Features

- Fullscreen kiosk mode
- Blocks common keyboard shortcuts to prevent exiting
- Loads a specified URL (currently set to <https://gkanev.com>)
- Secret exit combination (Shift+Tab+Caps Lock) for authorized personnel

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

To exit the application, use the secret key combination: Shift+Tab+Caps Lock (press all three keys simultaneously)

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
self.browser.load(QUrl("https://gkanev.com"))
```

Replace `"https://gkanev.com"` with your desired URL.

## Troubleshooting

1. **Exit combination doesn't work**: Ensure you're pressing Shift+Tab+Caps Lock simultaneously. If the issue persists, check if your keyboard is registering all key presses correctly.

2. **Page doesn't load**:
   - Check your internet connection.
   - Verify that the URL in the code is correct and accessible.
   - If using a local file, ensure the path is correct and the file exists.

3. **Application crashes on startup**:
   - Ensure all dependencies are correctly installed.
   - Check the console output for any error messages.

If problems persist, please open an issue on the GitHub repository with detailed information about the error and your system configuration.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For any questions or concerns, please open an issue on the GitHub repository.
