
from pymysql import connect
hostname = "127.0.0.1"
username = "root"
password = ""
database = "ppm_procedure"
class db():
    def __init__(self, hostname = hostname, username = username, password = password, database = database):
        try:
            self.mysql = connect(host=hostname, user=username, passwd=password, db=database, connect_timeout=0.1)
            self.connect = True
        except:
            self.connect = False
        if(self.connect == True):
            self.cursor = self.mysql.cursor()
    #模擬停車 return 0(成功) or 1(失敗)
    def test_stop(self):
        if(self.connect == True):
            self.cursor.execute("CALL stop_car()")
            RT = self.cursor.fetchall()
            if(len(RT) == 0):
                RT = "error"
            else:
                RT = RT[0][0]
        else:
            RT = 1
        return RT
    #查詢停車時間 return 開始時間
    def inquire_startT(self, licensePlateNumber:str, place:str):
        if(self.connect == True):
            self.cursor.execute(f"CALL inquire_startT('{licensePlateNumber}', '{place}')")
            RT = self.cursor.fetchall()
            if(len(RT) == 0):
                RT = "error"
            else:
                RT = RT[0][0]
        else:
            RT = "2023-05-22 00:00:00"
            RT = "error"
        return RT
    #查詢停車時間 return 暫停時間
    def inquire_stopT(self, licensePlateNumber:str, place:str):
        if(self.connect == True):
            self.cursor.execute(f"CALL inquire_stopT('{licensePlateNumber}', '{place}')")
            RT = self.cursor.fetchall()
            if(len(RT) == 0):
                RT = "error"
            else:
                RT = RT[0][0]
        else:
            RT = "2023-05-23 00:00:00"
            RT = "error"
        return RT