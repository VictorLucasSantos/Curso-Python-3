"""
Basico sobre Signal e Slots (eventos e documentação)
"""

import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QPushButton,
    QWidget,
)

app = QApplication(sys.argv)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle("Minha janela")

        self.botao = QPushButton("Texto do botão")
        self.botao.setStyleSheet("font-size: 40px")

        self.botao1 = QPushButton("Texto do botão")
        self.botao1.setStyleSheet("font-size: 40px")
        self.botao1.clicked.connect(self.segunda_acao_marcada)

        self.botao2 = QPushButton("Texto do botão")
        self.botao2.setStyleSheet("font-size: 40px")

        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

        self.layout.addWidget(self.botao, 1, 1, 1, 1)
        self.layout.addWidget(self.botao1, 1, 2, 1, 1)
        self.layout.addWidget(self.botao2, 3, 1, 1, 1)

        status_bar = self.statusBar()
        status_bar.showMessage("Mostrar mensagem na barra")

        menu = self.menuBar()
        self.primeiro_menu = menu.addMenu("Primeiro menu")
        self.primeira_acao = self.primeiro_menu.addAction("Primeira ação")
        self.primeira_acao.triggered.connect(self.muda_mensagem_da_status_bar)

        self.segunda_acao = self.primeiro_menu.addAction("Segunda ação")
        self.segunda_acao.setCheckable(True)
        self.segunda_acao.triggered.connect(self.segunda_acao_marcada)
        self.segunda_acao.hovered.connect(self.segunda_acao_marcada)

    @Slot()
    def muda_mensagem_da_status_bar(self):
        def inner():
            self.status_bar.showMessage("O meu slot foi executado")

        return inner

    @Slot()
    def segunda_acao_marcada(self):
        print("Está marcado?", self.segunda_acao.isChecked())

    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet("font-size: 80px;")
        return btn


if __name__ == "__main__":
    window = MyWindow()
    window.show()  # Central widget entre a hierarquia e
    app.exec()  ## loop da aplicação
