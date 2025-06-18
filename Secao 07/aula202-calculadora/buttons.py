from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from PySide6.QtCore import Slot
import math
from utils import isValidNumber
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # Tratamento para circular import
    from display import Display
    from info import Info
    from main_window import MainWindow


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
    def __init__(
        self, display: "Display", info: "Info", window: "MainWindow", *args, **kwargs
    ):
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
        self.window = window
        self._equation = ""
        self._equationInitialValue = "Sua conta"
        self._left = None
        self._right = None
        self._op = None
        self._equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        self.display.eqPressed.connect()
        self.display.delPressed.connect(self.display.backspace)
        self.display.clearPressed.connect()
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
            self._connectButtonClicked(button, self._clear)

        if text == "D":
            self._connectButtonClicked(button, self.display.backspace)

        if text in "+-/*^":
            self._connectButtonClicked(
                button, self._makeSlot(self._operatorClicked, button)
            )

    def _insertButtonTextToDisplay(self, button):
        button_text = button.text()
        newDisplayValue = self.display.text() + button_text
        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(button_text)
        # print(button.text(), checked)

    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self._equation = self._equationInitialValue
        self.display.clear()

    def _operatorClicked(self, button):
        print(button.text())
        text = button.text()  # +-*/...
        displayText = self.display.text()  # numero da esquerda
        self.display.clear()

        # Se foi informado o operador sem numeros validos
        if not isValidNumber(displayText) and self._left is None:
            self._showError("você não digitou nada")
            return

        if self._left is None:
            self._left = float(displayText)

        self._op = text
        self.equation = f"{self._left} {self._op} ??"

    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText) and self._left is None:
            self._showError("Não tem informações para colocar no valor da esquerda")
            return

        self._right = float(displayText)
        self._equation = f"{self._left} {self._op} {self._right}"
        result: float | str = "error"

        try:
            if "^" in self.equation and isinstance(self._left, float):
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            print("Zero Division Error")
        except OverflowError:
            print("Número muito grande")

            self.display.clear()
            self.info.setText(f"{self.equation} = {result}")
            self._right = None
            self._left = result

            if result == "error":
                self._left = None

    def _showError(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Warning)
        msgBox.exec()
