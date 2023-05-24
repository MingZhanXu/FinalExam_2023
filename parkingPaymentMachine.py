import os
import math
import datetime
from datetime import datetime as DT

import time
#計算規則:
#時間為無條件進位(30分1秒，則算60分)
class PPM():
    #初始化
    def __init__(self):        
        #需付金額
        self.money = 0
        #累積金額
        self.nowMoney = 0
        #開始時間
        self.startTime = DT.now()
        #結束時間
        self.endTime = None
        #跨日
        self.nextDay = 0
        #顯示用文字(減少計算量)
        self.printStr = ''
    #測試用(自行設定日期)
    #new_time = '%Y-%m-%d %H:%M:%S'
    def setStartTime(self,new_time = '2023-01-01 00:00:00'):
        error = 0
        try:
            self.startTime = DT.strptime(new_time,'%Y-%m-%d %H:%M:%S')
        except:
            error = 1
        if(error == 1):
            print('設定格式錯誤')
        return error
    #設定結束時間(測試用)
    #end_time = '%Y-%m-%d %H:%M:%S'
    def setEndTime(self,end_time = '2023-01-01 00:00:00'):
        error = 0
        try:
            self.endTime = DT.strptime(end_time,'%Y-%m-%d %H:%M:%S')
        except:
            error = 1
        if(error == 1):
            print('設定格式錯誤')
        return error
    #計算跨日
    def checkTime(self):
        #如果開始日期小於結束日期則互換
        if(self.endTime == None):
            self.endTime = DT.now()
        if(self.startTime > self.endTime):
            self.startTime,self.endTime = self.endTime,self.startTime
        self.nextDay = (self.endTime.date() - self.startTime.date()).days
        return self.nextDay
    #確認金額所需金額
    def checkNeedMoney(w,m):
        if(w < 5):
            #300/15 = 20
            if(m < 20):
                return m * 15
            return 300
        else:
            #420/20 = 21
            if(m < 21):
                return m * 20
            return 420
    #需要金額
    def needMoney(self):
        self.checkTime()
        if(self.nextDay != 0):
            tmp = self.startTime
            tmp = DT.strptime((tmp+datetime.timedelta(days=1)).date().strftime('%Y-%m-%d'),'%Y-%m-%d')
            self.money = PPM.checkNeedMoney((self.startTime.weekday()),int(math.ceil((tmp-self.startTime).total_seconds()/(60*30))))
            for i in range(self.nextDay - 1):
                self.money += PPM.checkNeedMoney(tmp.weekday(),48)
                tmp = DT.strptime((tmp+datetime.timedelta(days=1)).date().strftime('%Y-%m-%d'),'%Y-%m-%d')
            self.money += PPM.checkNeedMoney(self.endTime.weekday(),int(math.ceil((self.endTime-tmp).total_seconds()/(60*30))))
        else:
            self.money = PPM.checkNeedMoney((self.startTime.weekday()),int(math.ceil((self.endTime-self.startTime).total_seconds()/(60*30))))
        return self.money

    #正式用按鈕 無條件進位
    def check(self):
        self.endTime = DT.now()
        self.needMoney()
        self.printStr = f'開始停車時間 : {self.startTime}\n結束停車時間 : {self.endTime}\n'
        if(self.nextDay == 0):
            self.printStr += f'共停了 {int(math.ceil((self.endTime - self.startTime).total_seconds()/60))} 分鐘\n'
        elif(self.nextDay == 1):
            d1 = DT.strptime((self.startTime+datetime.timedelta(days=1)).date().strftime('%Y-%m-%d'),'%Y-%m-%d')
            d2 = DT.strptime((self.endTime).date().strftime('%Y-%m-%d'),'%Y-%m-%d')
            self.printStr += f'第一天共停了 {int(math.ceil((d1 - self.startTime).total_seconds()/60))} 分鐘，第二天共停了 {int(math.ceil((self.endTime -d2).total_seconds()/60))} 分鐘\n'
        else:
            d1 = DT.strptime((self.startTime+datetime.timedelta(days=1)).date().strftime('%Y-%m-%d'),'%Y-%m-%d')
            d2 = DT.strptime((self.endTime).date().strftime('%Y-%m-%d'),'%Y-%m-%d')
            self.printStr += f'第一天共停了 {int(math.ceil((d1 - self.startTime).total_seconds()/60))} 分鐘，最後一天共停了 {int(math.ceil((self.endTime -d2).total_seconds()/60))} 分鐘，並且在這段期間共停了 {self.nextDay - 1} 天\n'
        print(self.printStr)
    #測試用按鈕 無條件進位
    def testCheck(self):
        self.needMoney()
        self.printStr = f'開始停車時間 : {self.startTime}\n結束停車時間 : {self.endTime}\n'
        if(self.nextDay == 0):
            self.printStr += f'共停了 {int(math.ceil((self.endTime - self.startTime).total_seconds()/60))} 分鐘\n'
        elif(self.nextDay == 1):
            d1 = DT.strptime((self.startTime+datetime.timedelta(days=1)).date().strftime('%Y-%m-%d'),'%Y-%m-%d')
            d2 = DT.strptime((self.endTime).date().strftime('%Y-%m-%d'),'%Y-%m-%d')
            self.printStr += f'第一天共停了 {int(math.ceil((d1 - self.startTime).total_seconds()/60))} 分鐘，第二天共停了 {int(math.ceil((self.endTime -d2).total_seconds()/60))} 分鐘\n'
        else:
            d1 = DT.strptime((self.startTime+datetime.timedelta(days=1)).date().strftime('%Y-%m-%d'),'%Y-%m-%d')
            d2 = DT.strptime((self.endTime).date().strftime('%Y-%m-%d'),'%Y-%m-%d')
            self.printStr += f'第一天共停了 {int(math.ceil((d1 - self.startTime).total_seconds()/60))} 分鐘，最後一天共停了 {int(math.ceil((self.endTime -d2).total_seconds()/60))} 分鐘，並且在這段期間共停了 {self.nextDay - 1} 天\n'
        print(self.printStr)
        print(f'需付 {self.money} 元\n')
    #輸入硬幣 c_mm 硬幣大小 c_m 硬幣磁力
    def pay(self, c_mm, c_m):
        #if與elif的物品會存放在一個暫存箱
        if(c_mm == 22 and c_m == 1):
            self.nowMoney += 5
        elif(c_mm == 26 and c_m == 2):
            self.nowMoney += 10
        elif(c_mm == 28 and c_m == 3):
            self.nowMoney += 50
        #直接歸還
        else:
            os.system('cls')
            print(self.printStr)
            print('\n\n這不是可識別的硬幣')
            return 1
        needMoneyD = self.nowMoney - self.money
        if(needMoneyD < 0):
            os.system('cls')
            print(self.printStr)
            print(f'需付 {self.money} 元\n已付 {self.nowMoney} 元，還須付 {-needMoneyD} 元')
            return 0
        if(needMoneyD > 0):
            os.system('cls')
            print(self.printStr)
            print(f'需付 {self.money} 元\n已付 {self.nowMoney} 元，將退還 {needMoneyD} 元')
            self.checkPay()
        else:
            os.system('cls')
            print(self.printStr)
            print(f'需付 {self.money} 元\n已付 {self.nowMoney} 元')
            self.checkPay()
    #取消付款
    def cancel(self):
        self.nowMoney = 0
        print('執行退幣動作')
    #正式用按鈕 無條件進位
    def checkPay(self):
        needMoneyD = self.nowMoney - self.money
        pay = input("是否確認付款(Y/N)")
        if(pay == 'Y'):
            if(needMoneyD == 0):
                os.system('cls')
                print('已完成付款，以下是帳單\n\n')
                print(self.printStr)
                print(f'總共 {self.money} 元')
                return 0
            else:
                os.system('cls')
                print(f'已完成付款，並將退回 {needMoneyD} 元，以下是帳單\n\n')
                print(self.printStr)
                print(f'總共 {self.money} 元')
                return 0
        else:
            self.cancel()

if __name__ == '__main__':
    os.system('cls')
    my = PPM()
    my.setStartTime('2023-05-25 23:59:59')
    my.setEndTime('2023-05-26 00:30:01')
    my.needMoney()
    my.testCheck()
    while(my.pay(28,3) == 0):
        time.sleep(1)