from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

def main():
    kwanseigo = kggo()
    station = kggo.ingostation()
    hour = kggo.gohour()
    minute = kggo.gominute()
    kggo.gosanda(station, hour, minute)

class kggo(): #ブラウザでの操作は基本headless modeで行う →→→最後に実装すれば良い
 
    def ingostation(): #出発する駅名
        gosta = input("出発する駅")
        return gosta

    def gohour(): #出発する時間のhour部分
        gotimehhstr = input("駅を出発する時間 hour")
        #gotimehour = int(gotimehhstr) - 1
        #return gotimehour
        return gotimehhstr
        
    def gominute(): #出発する時間のminute部分
        gotimemmstr = input("駅を出発する時間 minite")
        #gotimeminute = int(gotimemmstr) - 1
        #return gotimeminute
        return gotimemmstr

        
    def gosanda(gostation, hour, minute): #出発駅からの電車の時刻表
        browser = webdriver.Chrome()
        url = "https://transit.yahoo.co.jp/"  #yahoo乗り換え
        browser.get(url)
        
        inputfrom = browser.find_element_by_name('from')
        inputfrom.send_keys('gostation')

        inputto = browser.find_element_by_name('to')
        inputto.send_keys('三田')

        timeselecthh = browser.find_element_by_id('hh')
        selecthour = Select(timeselecthh)
        selecthour.select_by_value(hour)

        timeselectmm = browser.find_element_by_id('mm')
        selectminute = Select(timeselectmm)
        selectminute.select_by_value(minute)

        submit = browser.find_element_by_id('searchModuleSubmit')
        submit.click()

        sleep(30)
    
    """
    def sndkg():
    #三田駅から関学の時刻表
    #pdfからよみこむ

    def shinsndkg(): #新三田駅から関学の時刻表
    #pdfからよみこむ
    

    def print():
    #出発時間を出力する
    #新三田に到着する時間、関学行きにのる時間を出力
    #関学に到着する時間を出力
    """

    
if __name__ == "__main__":
    main()

#運行状況をスクレイピング
