from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MININUM_WIDTH
from utils import isEmpty, isNumOrDot


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px;")
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.minimumWidth = MININUM_WIDTH
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])

    def keyPressEvent(self, event: QKeyEvent):
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isOperator = key in [
            KEYS.Key_Plus,
            KEYS.Key_Slash,
            KEYS.Key_Minus,
            KEYS.Key_Asterisk,
            KEYS.Key_P,
        ]

        if isEnter:
            self.eqPressed.emit()
            event.accept()
            return

        if isOperator:
            if text.lower() == "p":
                text = "^"
            self.operatorPressed.emit(text)
            event.accept()
            return

        if isEsc:
            self.clearPressed.emit()
            event.ignore()
            return

        if isDelete or text.lower() == "c":
            self.delPressed.emit()
            event.accept()
            return

        if isEmpty(text):
            event.accept()
            return

        if isNumOrDot(text):
            self.inputPressed.emit(text)
            event.accept()
            return
