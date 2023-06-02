from PPM_window import keyboardWindow
from PySide6.QtGui import  Qt


def test_hello(qtbot):
    app = keyboardWindow()
    qtbot.addWidget(app)
    qtbot.mouseClick(app.ui.btn_A, Qt.LeftButton)
    assert app.ui.edit_inquire.text() == "A"