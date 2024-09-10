import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QProgressBar
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
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

        self.progress_bar = QProgressBar(self)
        layout.addWidget(self.progress_bar)

        self.browser = QWebEngineView()
        self.browser.page().loadStarted.connect(self.load_started)
        self.browser.page().loadProgress.connect(self.load_progress)
        self.browser.page().loadFinished.connect(self.load_finished)
        self.browser.page().loadFinished.connect(self.check_load_status)
        layout.addWidget(self.browser)

        self.load_url("https://gkanev.com")

        self.exit_keys = set()

    def load_url(self, url):
        self.browser.setUrl(QUrl(url))

    def load_started(self):
        self.progress_bar.setValue(0)
        self.progress_bar.show()

    def load_progress(self, progress):
        self.progress_bar.setValue(progress)

    def load_finished(self, success):
        self.progress_bar.hide()

    def check_load_status(self, success):
        if not success:
            error_html = f"""
            <html>
            <body style="display:flex;justify-content:center;align-items:center;height:100vh;font-family:Arial,sans-serif;">
                <div style="text-align:center;">
                    <h1>Error Loading Page</h1>
                    <p>Unable to load the specified URL. Please check your internet connection and try again.</p>
                    <p>If the problem persists, contact your system administrator.</p>
                </div>
            </body>
            </html>
            """
            self.browser.setHtml(error_html)

    def keyPressEvent(self, event):
        key = event.key()
        self.exit_keys.add(key)
        
        if set([Qt.Key_Shift, Qt.Key_Tab, Qt.Key_CapsLock]).issubset(self.exit_keys):
            self.close()
        else:
            event.ignore()

    def keyReleaseEvent(self, event):
        key = event.key()
        if key in self.exit_keys:
            self.exit_keys.remove(key)

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