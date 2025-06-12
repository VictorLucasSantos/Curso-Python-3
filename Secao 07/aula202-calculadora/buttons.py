from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from PySide6.QtCore import Slot
from utils import isValidNumber
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # Tratamento para circular import
    from display import Display
    from info import Info


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        # self.setCheckable(True)
        # self.setProperty("cssClass", "specialButton")


class ButtonsGrid(QGridLayout):
    def __init__(self, display: "Display", info: "Info", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._gridMask = [
            ["C", "D", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["N", "0", ".", "="],
        ]
        self.display = display
        self.info = info
        self._equation = ""
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        for rowNumber, rowData in enumerate(self._gridMask):
            for columNumber, buttonText in enumerate(rowData):
                button = Button(buttonText)

                if buttonText not in "0123456789.":
                    button.setProperty("cssClass", "specialButton")
                    self._configSpecialButton(button)

                self.addWidget(button, rowNumber, columNumber)
                slot = self._makeSlot(self._insertButtonTextToDisplay, button)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)

        return realSlot

    def _configSpecialButton(self, button):
        text = button.text()

        if text == "C":
            # slot = self._makeSlot(self.display.clear)
            self._connectButtonClicked(button, self._clear)

        if text == "+-/*":
            # slot = self._makeSlot(self.display.clear)
            self._connectButtonClicked(button, self._clear)

    def _insertButtonTextToDisplay(self, button):
        button_text = button.text()
        newDisplayValue = self.display.text() + button_text
        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(button_text)
        # print(button.text(), checked)

    def _clear(self):
        self.display.clear()
        print("Algo mais")
