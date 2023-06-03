from PPM_window import keyboardWindow
from PySide6.QtGui import  Qt
import pytest
class Test_keyboard():
    #測試鍵盤按鍵A~Z
    @pytest.mark.parametrize(argnames='keyStr',argvalues = [chr(ord("A") + i)for i in range(23)])
    def test_keyStr(self,qtbot, keyStr:str):
        app = keyboardWindow()
        qtbot.addWidget(app)
        btn = "btn_" + keyStr
        qtbot.mouseClick(getattr(app.ui,btn), Qt.LeftButton)
        assert app.ui.edit_inquire.text() == keyStr    