import sys
from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from display import Display
from PySide6.QtGui import QIcon
from buttons import Button, ButtonsGrid
from info import Info
from styles import setupTheme
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    info = Info("2.0 ^10.0 = 1024")
    window.addWidgetToVLayout(info)

    display = Display()
    window.addWidgetToVLayout(display)

    buttonsGrid = ButtonsGrid(display=display, info=info, window=window)
    buttonsGrid._makeGrid()
    window.vLayout.addLayout(buttonsGrid)

    window.adjustFixedSize()
    window.show()
    app.exec()
