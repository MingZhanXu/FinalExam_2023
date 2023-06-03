
from lib.PPM.PPM_window import keyboardWindow
from PySide6.QtGui import  Qt
import pytest
class test_keyboard():
    #測試設定開始時間(正確 回傳值)
    @pytest.mark.parametrize(argnames='keyStr',argvalues = [chr(ord("A") + i)for i in range(23)])
    def test_keyStr(self,qtbot, keyStr:str):
        app = keyboardWindow()
        qtbot.addWidget(app)
        btn = "app.ui.btn_" + keyStr
        qtbot.mouseClick(getattr(btn), Qt.LeftButton)
        assert app.ui.edit_inquire.text() == keyStr