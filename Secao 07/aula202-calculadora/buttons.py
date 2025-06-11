from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE, SMALL_FONT_SIZE
from PySide6.QtCore import Slot
from utils import isValidNumber
from display import Display


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(SMALL_FONT_SIZE)
        self.setFont(font)
        self.setCheckable(True)
        # self.setProperty("cssClass", "specialButton")


class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._gridMask = [
            ["C", "D", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["N", "0", ".", "="],
        ]
        self.display = display
        self._makeGrid()

    def _makeGrid(self):
        for rowNumber, rowData in enumerate(self._gridMask):
            for columNumber, buttonText in enumerate(rowData):
                button = Button(buttonText)

                if buttonText not in "0123456789.":
                    button.setProperty("cssClass", "specialButton")

                self.addWidget(button, rowNumber, columNumber)
                buttonSlot = self._makeButtonDisplaySlot(
                    self._insertButtonTextToDisplay, button
                )
                button.clicked.connect(buttonSlot)

    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(checked):
            func(checked, *args, **kwargs)

        return realSlot

    def _insertButtonTextToDisplay(self, checked, button):
        button_text = button.text()
        newDisplayValue = self.display.text() + button_text
        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(button_text)
        # print(button.text(), checked)
