from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit
from PySide6.QtCore import QSize
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(400, 300))
        self.setWindowTitle("GUI Pulse")

        text_edit = QTextEdit(self)
        text_edit.setGeometry(0, 0, 360, 260)
        
        
        text_edit.setText("")
        
        
        text_edit.setReadOnly(True)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())