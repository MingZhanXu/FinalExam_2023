from PySide6.QtWidgets import (QApplication, QMainWindow, QButtonGroup)
from PySide6.QtCore import (QFile)
from untitled_ui import Ui_Form
from untitled_main import MainWindow
from PySide6.QtGui import  Qt

def test_hello(qtbot):
    app = MainWindow()
    qtbot.addWidget(app)
    qtbot.mouseClick(app.ui.btn_A, Qt.LeftButton)
    assert app.ui.edit_inquire.text() == "A"