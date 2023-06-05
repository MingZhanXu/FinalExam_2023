from PPM_window import keyboardWindow
from PySide6.QtGui import  Qt
import pytest
#測試鍵盤
@pytest.mark.keyboard
class Test_keyboard():
    #測試鍵盤按鍵A~Z
    @pytest.mark.keyboard_AZN
    @pytest.mark.parametrize(argnames='keyStr',argvalues = [chr(ord("A") + i)for i in range(23)])
    def test_key_AZN(self,qtbot, keyStr:str):
        app = keyboardWindow()
        qtbot.addWidget(app)
        btn = "btn_" + keyStr
        qtbot.mouseClick(getattr(app.ui,btn), Qt.LeftButton)
        assert app.ui.edit_inquire.text() == keyStr
    #測試鍵盤輸入文字XXX-NNNN
    @pytest.mark.keyboard_XXX_NNNN
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
    @pytest.mark.keyboard_del
    @pytest.mark.parametrize(argnames='keyStr, Del, txt',argvalues = [["A10BC35ZX120","000100011000", "AC"],
                                                                      ["121SAASD3213A","1110010011110", "SAS-"],
                                                                      ["121SAASD3213A","0110010011110", "SAS-"],
                                                                      ["121SAASD3213A","0110010011100", "SAS-3"],
                                                                      ["121SAASD3213A","0110010011111", "SA"]])
    def test_keyDel(self,qtbot, keyStr:str, Del:str, txt:str):
        app = keyboardWindow()
        qtbot.addWidget(app)
        i = 0
        for AZN in keyStr:
            if (AZN >= "0" and AZN <= "9"):
                btn = "btn_n" + AZN
            else:
                btn = "btn_" + AZN
            qtbot.mouseClick(getattr(app.ui,btn), Qt.LeftButton)
            if (Del[i] == "1"):
                qtbot.mouseClick(app.ui.btn_del, Qt.LeftButton)
            i+=1
        assert app.ui.edit_inquire.text() == txt
    #測試鍵盤cls
    @pytest.mark.keyboard_cls
    @pytest.mark.parametrize(argnames='keyStr, clear, txt',argvalues = [["A3B5C6","001000", "C"],
                                                                        ["AAB3C5DD","10000000", "ABC-5"],
                                                                        ["SDA1234","0000001", ""]])
    def test_keyCls(self,qtbot, keyStr:str, clear:str, txt:str):
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
                qtbot.mouseClick(app.ui.btn_cls, Qt.LeftButton)
            i+=1
        assert app.ui.edit_inquire.text() == txt
    #測試鍵盤inquire的畫面切換功能
    @pytest.mark.keyboard_inquire
    @pytest.mark.keyboard_inquire_isShow
    @pytest.mark.parametrize(argnames='keyStr, KW, PW',argvalues = [["ABC123", 1, 0],
                                                                    ["1234ABC", 1, 0],
                                                                    ["ABC1234", 0, 1]])
    def test_keyInquire_isShow(self,qtbot, keyStr:str, KW:int, PW:int):
        app = keyboardWindow()
        qtbot.addWidget(app)
        for AZN in keyStr:
            if (AZN >= "0" and AZN <= "9"):
                btn = "btn_n" + AZN
            else:
                btn = "btn_" + AZN
            qtbot.mouseClick(getattr(app.ui,btn), Qt.LeftButton)
        qtbot.mouseClick(app.ui.btn_inquire, Qt.LeftButton)
        assert (app.isShow == KW and app.PW.isShow == PW)
    #測試鍵盤inquire查詢的結果
    @pytest.mark.keyboard_inquire
    @pytest.mark.keyboard_inquire_sqlReturnTxt
    @pytest.mark.parametrize(argnames='keyStr, error',argvalues = [["ABC1234", 1],
                                                                   ["ABC1234", 1],
                                                                   ["ABC1234", 0]])
    def test_keyInquire_sqlReturnTxt(self,qtbot, keyStr:str, error:int):
        app = keyboardWindow()
        qtbot.addWidget(app)
        for AZN in keyStr:
            if (AZN >= "0" and AZN <= "9"):
                btn = "btn_n" + AZN
            else:
                btn = "btn_" + AZN
            qtbot.mouseClick(getattr(app.ui,btn), Qt.LeftButton)
        qtbot.mouseClick(app.ui.btn_inquire, Qt.LeftButton)
        printTxt = app.PW.ui.label_print.text()
        if(error == 1):
            assert (printTxt == "查無此資料，十秒後返回")
        elif(error == 0 and app.PW.db.connect == False):
            assert (printTxt == "查無此資料，十秒後返回")
        else:
            assert ( printTxt == app.PW.PPM.check())