import sys
from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    label = QLabel("Qualquer coisa")
    window.v_layout.addWidget(label)

    window.adjustFixedSize()
    window.show()
    app.exec()
