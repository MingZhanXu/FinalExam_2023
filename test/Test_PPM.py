import pytest
from lib.PPM.PPM import PPM

#正確為C，錯誤為M
#CReturn 正確回傳為 0
CReturn = 0
#MReturn 錯誤回傳為 1 可設定為 0 來讓測試顯示錯誤
MReturn = 1

#命名格式
#class Test_C(正確)或M(錯誤)函數
#def test_C(正確)或M(錯誤)_函數_(內容_)回傳值或資料類型

#測試正確用法setStartTime函數
@pytest.mark.correct
@pytest.mark.setStartTime
class Test_CSetStartTime():
#測試設定開始時間(正確 回傳值)
    @pytest.mark.parametrize(argnames='data',argvalues = ['2023-01-01 00:00:00','2023-01-01 23:59:59','2024-02-29 00:00:00'])
    def test_C_setStartTime_return(self, data:str):
        my = PPM()
        assert my.setStartTime('2023-01-01 00:00:00') == CReturn
    #測試設定開始時間(正確 時間)
    @pytest.mark.parametrize(argnames='data',argvalues = ['2023-01-01 00:00:00','2023-01-01 23:59:59','2024-02-29 00:00:00'])
    def test_C_setStartTime_time(self, data:str):
        my = PPM()
        my.setStartTime(data)
        assert my.startTime.strftime("%Y-%m-%d %H:%M:%S") == data
#測試錯誤用法setStartTime函數
@pytest.mark.mistake
@pytest.mark.setStartTime
class Test_MSetStartTime():
    #測試設定開始時間(錯誤 格式 回傳值)
    @pytest.mark.parametrize(argnames='data',argvalues = [ '2023:01-01 00:00:00', '2023-01:01 00:00:00',
                                                           '2023-01-01-00:00:00', '2023-01-01 00-00:00',
                                                           '2023-01-01 00:00-00'])
    def test_M_setStartTime_format_return(self, data:str):
        my = PPM()
        assert my.setStartTime(data) == MReturn
    #測試設定開始時間(錯誤 資料(日期) 回傳值)
    @pytest.mark.parametrize(argnames='data',argvalues = [ '0000-01-01 00:00:00', '2023-00-01 00:00:00',
                                                           '2023-13-01 00:00:00', '2023-01-00 00:00:00',
                                                           '2023-01-32 00:00:00', '2023-02-29 00:00:00'])
    def test_M_setStartTime_data_return(self, data:str):
        my = PPM()
        assert my.setStartTime(data) == MReturn
    
#測試正確用法setEndTime函數
@pytest.mark.correct
@pytest.mark.setEndTime
class Test_CSetEndTime():
#測試設定開始時間(正確 回傳值)
    @pytest.mark.parametrize(argnames='data',argvalues = ['2023-01-01 00:00:00','2023-01-01 23:59:59','2024-02-29 00:00:00'])
    def test_C_setEndTime_return(self, data:str):
        my = PPM()
        assert my.setEndTime(data) == CReturn
    #測試設定開始時間(正確 時間)
    @pytest.mark.parametrize(argnames='data',argvalues = ['2023-01-01 00:00:00','2023-01-01 23:59:59','2024-02-29 00:00:00'])
    def test_C_setEndTime_time(self, data:str):
        my = PPM()
        my.setEndTime(data)
        assert my.endTime.strftime("%Y-%m-%d %H:%M:%S") == data
#測試錯誤用法setEndTime函數
@pytest.mark.mistake
@pytest.mark.setEndTime
class Test_MSetEndTime():
    #測試設定開始時間(錯誤 格式 回傳值)
    @pytest.mark.parametrize(argnames='data',argvalues = [ '2023:01-01 00:00:00', '2023-01:01 00:00:00',
                                                           '2023-01-01-00:00:00', '2023-01-01 00-00:00',
                                                           '2023-01-01 00:00-00'])
    def test_M_setEndTime_format_return(self, data:str):
        my = PPM()
        assert my.setEndTime(data) == MReturn
    #測試設定開始時間(錯誤 資料(日期) 回傳值)
    @pytest.mark.parametrize(argnames='data',argvalues = [ '0000-01-01 00:00:00', '2023-00-01 00:00:00',
                                                           '2023-13-01 00:00:00', '2023-01-00 00:00:00',
                                                           '2023-01-32 00:00:00', '2023-02-29 00:00:00'])
    def test_M_setEndTime_data_return(self, data:str):
        my = PPM()
        assert my.setEndTime(data) == MReturn
  
@pytest.mark.correct
@pytest.mark.checkTime
#測試正確用法checkTime函數
class Test_CCheckTime():
    #測試回傳時間差
    @pytest.mark.parametrize(argnames='startD, endD, RT',
                             argvalues = [('2023-01-01 00:00:00','2023-01-01 00:00:00', 0),
                                          ('2023-01-01 00:00:00','2023-01-01 23:59:59', 0),
                                          ('2023-01-01 23:59:59','2023-01-01 00:00:00', 0),
                                          ('2023-01-02 00:00:00','2023-01-01 00:00:00', 1)])
    def test_C_checkTime_return(self, startD:str, endD:str, RT:int):
        my = PPM()
        my.setStartTime(startD)
        my.setEndTime(endD)
        assert my.checkTime() == RT

@pytest.mark.correct
@pytest.mark.checkNeedMoney
#測試正確用法checkNeedMoney函數
class Test_CCheckNeedMoney():
    @pytest.mark.parametrize(argnames = 'w, m, RT', argvalues = [(0, 1, 15), (0, 8, 120), (0, 19, 285), (0, 21, 300),
                                                                 (4, 1, 15), (4, 8, 120), (4, 19, 285), (4, 21, 300),
                                                                 (5, 1, 20), (5, 8, 160), (5, 19, 380), (5, 22, 420),
                                                                 (6, 1, 20), (6, 8, 160), (6, 19, 380), (6, 22, 420),
                                                                 #不正確的輸入
                                                                 (-1, 1, 15), (-1, 8, 120), (-1, 19, 285), (-1, 21, 300),
                                                                 (100, 1, 20), (100, 8, 160), (100, 19, 380), (100, 22, 420)])
    #測試計算數值
    def test_C_checkNeedMoney(self, w:int, m:int, RT:int):
        assert PPM.checkNeedMoney(w, m) == RT

@pytest.mark.correct
@pytest.mark.needMoney
#測試正確用法needMoney函數
class Test_CNeedMoney():
    #測試needMoney計算結果
    @pytest.mark.parametrize(argnames='startD, endD, RT', argvalues=[('2023-05-22 00:00:00','2023-05-22 00:00:00', 0),
                                                                     ('2023-05-22 00:00:00','2023-05-22 00:00:01', 15),
                                                                     ('2023-05-22 00:00:01','2023-05-22 00:00:00', 15),
                                                                     ('2023-05-22 00:00:00','2023-05-23 00:00:00', 300),
                                                                     ('2023-05-22 00:00:00','2023-05-22 09:30:01', 300),
                                                                     ('2023-05-26 00:00:00','2023-05-27 00:00:00', 300),
                                                                     ('2023-05-26 00:00:00','2023-05-27 00:00:01', 320),
                                                                     ('2023-05-26 00:00:00','2023-05-27 10:00:01', 720),
                                                                     ('2023-05-26 00:00:00','2023-05-27 10:30:01', 720)])
    def test_C_NeedMoney(self, startD:str, endD:str, RT:int):
        my = PPM()
        my.setStartTime(startD)
        my.setEndTime(endD)
        assert my.needMoney() == RT

@pytest.mark.correct
@pytest.mark.testCheck
class Test_CTestCheck():
    #測試字串是否正確
    @pytest.mark.parametrize(argnames='startD, endD, RT', argvalues=[('2023-05-22 00:00:00','2023-05-22 00:00:00', '開始停車時間 : 2023-05-22 00:00:00\n結束停車時間 : 2023-05-22 00:00:00\n共停了 0 分鐘\n\n需付 0 元\n'),
                                                                     ('2023-05-22 00:00:00','2023-05-22 00:00:01', '開始停車時間 : 2023-05-22 00:00:00\n結束停車時間 : 2023-05-22 00:00:01\n共停了 1 分鐘\n\n需付 15 元\n'),
                                                                     ('2023-05-22 00:00:01','2023-05-22 00:00:00', '開始停車時間 : 2023-05-22 00:00:00\n結束停車時間 : 2023-05-22 00:00:01\n共停了 1 分鐘\n\n需付 15 元\n'),
                                                                     ('2023-05-22 00:00:00','2023-05-23 00:00:00', '開始停車時間 : 2023-05-22 00:00:00\n結束停車時間 : 2023-05-23 00:00:00\n第一天共停了 1440 分鐘，第二天共停了 0 分鐘\n\n需付 300 元\n'),
                                                                     ('2023-05-22 00:00:00','2023-05-24 00:00:00', '開始停車時間 : 2023-05-22 00:00:00\n結束停車時間 : 2023-05-24 00:00:00\n第一天共停了 1440 分鐘，最後一天共停了 0 分鐘，並且在這段期間共停了 1 天\n\n需付 600 元\n'),
                                                                     ('2023-05-22 23:30:00','2023-05-24 00:00:00', '開始停車時間 : 2023-05-22 23:30:00\n結束停車時間 : 2023-05-24 00:00:00\n第一天共停了 30 分鐘，最後一天共停了 0 分鐘，並且在這段期間共停了 1 天\n\n需付 315 元\n'),
                                                                     ('2023-05-22 23:30:00','2023-05-27 00:00:01', '開始停車時間 : 2023-05-22 23:30:00\n結束停車時間 : 2023-05-27 00:00:01\n第一天共停了 30 分鐘，最後一天共停了 1 分鐘，並且在這段期間共停了 4 天\n\n需付 1235 元\n'),
                                                                     ('2023-05-22 23:30:00','2023-05-28 00:00:01', '開始停車時間 : 2023-05-22 23:30:00\n結束停車時間 : 2023-05-28 00:00:01\n第一天共停了 30 分鐘，最後一天共停了 1 分鐘，並且在這段期間共停了 5 天\n\n需付 1655 元\n'),
                                                                     ('2023-05-22 23:30:00','2023-05-28 00:00:01', '開始停車時間 : 2023-05-22 23:30:00\n結束停車時間 : 2023-05-28 00:00:01\n第一天共停了 30 分鐘，最後一天共停了 1 分鐘，並且在這段期間共停了 5 天\n\n需付 1655 元\n'),
                                                                     ('2023-05-22 23:30:00','2023-05-28 10:00:01', '開始停車時間 : 2023-05-22 23:30:00\n結束停車時間 : 2023-05-28 10:00:01\n第一天共停了 30 分鐘，最後一天共停了 601 分鐘，並且在這段期間共停了 5 天\n\n需付 2055 元\n'),
                                                                     ('2023-05-22 23:30:00','2023-05-28 11:00:00', '開始停車時間 : 2023-05-22 23:30:00\n結束停車時間 : 2023-05-28 11:00:00\n第一天共停了 30 分鐘，最後一天共停了 660 分鐘，並且在這段期間共停了 5 天\n\n需付 2055 元\n')])
    def test_C_testCheck(self, startD:str, endD:str, RT:str):
        my = PPM()
        my.setStartTime(startD)
        my.setEndTime(endD)
        rt = my.testCheck()
        assert rt == RT
