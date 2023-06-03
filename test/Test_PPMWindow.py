from PPM_window import keyboardWindow
from PySide6.QtGui import  Qt
import pytest
#測試鍵盤
@pytest.mark.keyboard
class Test_keyboard():
    #測試鍵盤按鍵A~Z
    @pytest.mark.parametrize(argnames='keyStr',argvalues = [chr(ord("A") + i)for i in range(23)])
    def test_key_AZN(self,qtbot, keyStr:str):
        app = keyboardWindow()
        qtbot.addWidget(app)
        btn = "btn_" + keyStr
        qtbot.mouseClick(getattr(app.ui,btn), Qt.LeftButton)
        assert app.ui.edit_inquire.text() == keyStr
    #測試鍵盤輸入文字XXX-NNNN
    @pytest.mark.parametrize(argnames='keyStr, txt',argvalues = [["A10BC35ZX120","ABC-3512"],
                                                                 ["121SAASD3213A","SAA-3213"],
                                                                 ["AS1232131HZ12","ASH-12"],
                                                                 ["ASDADSAADA","ASD-"],
                                                                 ["12312313131544646",""]])
    def test_keyStr(self,qtbot, keyStr:str, txt:str):
        app = keyboardWindow()
        qtbot.addWidget(app)
        for AZN in keyStr:
            if (AZN >= "0" and AZN <= "9"):
                btn = "btn_n" + AZN
            else:
                btn = "btn_" + AZN
            qtbot.mouseClick(getattr(app.ui,btn), Qt.LeftButton)
        assert app.ui.edit_inquire.text() == txt
    #測試鍵盤del與-填充
    @pytest.mark.parametrize(argnames='keyStr, clear, txt',argvalues = [["A10BC35ZX120","000100011000", "AC"],
                                                                        ["121SAASD3213A","1110010011110", "SAS-"],
                                                                        ["121SAASD3213A","0110010011110", "SAS-"],
                                                                        ["121SAASD3213A","0110010011100", "SAS-3"]])
    def test_keyDel(self,qtbot, keyStr:str, clear:str, txt:str):
        app = keyboardWindow()
        qtbot.addWidget(app)
        i = 0
        for AZN in keyStr:
            if (AZN >= "0" and AZN <= "9"):
                btn = "btn_n" + AZN
            else:
                btn = "btn_" + AZN
            qtbot.mouseClick(getattr(app.ui,btn), Qt.LeftButton)
            if (clear[i] == "1"):
                qtbot.mouseClick(app.ui.btn_del, Qt.LeftButton)
            i+=1
        assert app.ui.edit_inquire.text() == txt