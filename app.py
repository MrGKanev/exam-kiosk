import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt, QUrl
from pynput import keyboard

class KioskWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exam Kiosk")
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.showFullScreen()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://gkanev.com"))
        layout.addWidget(self.browser)

    def keyPressEvent(self, event):
        # Ignore most key events to prevent exiting fullscreen
        if event.key() not in [Qt.Key_F11, Qt.Key_Escape]:
            event.ignore()
        else:
            super().keyPressEvent(event)

def on_press(key):
    try:
        # Block Alt+Tab, Win key, Cmd key
        if key in [keyboard.Key.alt_l, keyboard.Key.alt_r, keyboard.Key.tab,
                   keyboard.Key.cmd, keyboard.Key.cmd_l, keyboard.Key.cmd_r]:
            return False
    except AttributeError:
        pass
    return True

def main():
    app = QApplication(sys.argv)
    
    # Start key listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    window = KioskWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()