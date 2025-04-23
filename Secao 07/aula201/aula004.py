"""
QMainWindow e centralWidget
 -> QApplication (app)
   -> QMainWindow (window->setCentralWidget)
       -> CentralWidget (central_widget)
           -> Layout (layout)
               -> Widget 1 (botao1)
               -> Widget 2 (botao2)
               -> Widget 3 (botao3)
   -> show
 -> exec
"""

import sys

from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
    QMainWindow,
)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle("Minha janela")

botao = QPushButton("Texto do botão ")
botao.setStyleSheet("font-size: 80px;")

botao1 = QPushButton("Texto do botão 1")
botao1.setStyleSheet("font-size: 80px;")

botao2 = QPushButton("Texto do botão 2")
botao2.setStyleSheet("font-size: 80px;")

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao1, 1, 2, 1, 1)
layout.addWidget(botao2, 3, 1, 1, 2)


def slot_example(status_bar):
    status_bar.showMessage("Slot executado")


status_bar = window.statusBar()
status_bar.showMessage("Mostrar mensagem na barra")

menu = window.menuBar()
primeiro_menu = menu.addMenu("Primeiro menu")
primeira_acao = primeiro_menu.addAction("Primeira ação")
primeira_acao.triggered.connect(lambda: slot_example(status_bar))

window.show()  # Central widget entre a hierarquia e
app.exec()  ## loop da aplicação
