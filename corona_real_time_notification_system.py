
from plyer import notification
import requests
from bs4 import BeautifulSoup as soup
import time
def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C://Users//satyadeep singh//Downloads//coronavirus.ico",
        timeout = 15
    )
def getData(url):
    r = requests.get(url)
    return r.text
if __name__ == "__main__":
    # notifyMe("Hey Satyadeep","Lets stop the spread of this virus. #staysafe #gocoronago ")
    myHtmlData = getData("https://www.mohfw.gov.in/")
    s = soup(myHtmlData, 'html.parser')
    # print(s.prettify())
    myDataStr = ""
    for tr in s.find_all('tbody')[1].find_all('tr'):
        myDataStr += tr.get_text()
    myDataStr = myDataStr[1:]
    itemList = myDataStr.split("\n\n")
    states = ['Punjab', 'Rajasthan', 'Uttar Pradesh', 'Maharashtra', 'Delhi']
    for item in itemList[0:22]:
        dataList = item.split('\n')
        if dataList[1] in states:
            print(dataList)
            nTitle = 'Cases of Covid-19'
            nText = f"State - {dataList[1]}\nIndian : {dataList[2]} & Foreign : {dataList[3]}\nCured : {dataList[4]}\nDeaths : {dataList[5]}"
            notifyMe(nTitle, nText)
            time.sleep(2)
