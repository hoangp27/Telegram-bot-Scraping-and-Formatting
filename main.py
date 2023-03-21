
import os
import telebot
#import requests
#from bs4 import BeautifulSoup
import keep_alive
import pandas as pd

keep_alive.keep_alive()

Web Scraping coinlist
URL = "https://www.binance.com/en/futures/trading-rules/perpetual"
page = requests.get(URL)
soup = BeautifulSoup(page.content,"html.parser")
results= soup.find(id="__APP")
coinPairList = soup.find_all("td", class_="rc-table-cell rc-table-cell-fix-left rc-table-cell-fix-left-last")


CoinList = pd.read_csv("coinlist.csv")
NumberList = []


for x in range(0, len(CoinList)):
  CoinList[x] = "#" + CoinList[x]
  #CoinList.append(coinPair)



print(CoinList)

my_API_key = os.environ['API']
bot = telebot.TeleBot(my_API_key)


def check_float(potential_float):
  try:
    float(potential_float)
  except ValueError:
    return False
  else:
    return True

def target_detect (message): 
  message_element = message.text.split()
  for text in message_element:
    #print(text)
    if check_float(text)== True:
      NumberList.append(text)
  NumberList.sort(key = float)
  print(NumberList)
 
  
def coin_detect (message):
  message_element = message.text.split()
  #request = message_element[1].replace("/","")
  request = message_element[0]
  #print(request)
  for coin in CoinList:
    if request == coin:
      target_detect(message)
      return True
  return False

@bot.message_handler(func= coin_detect)
def send_signal(message):
  if len(NumberList) >= 7:
    request = message.text.split()[0]
    signal1 = ""
    signal2 =""
    signal1 = "signal buy " + request + "\n\n" + "❇️ Buy Price: "+ NumberList[1] + "\n" 
    signal2 = "signal buy " + request + "\n\n" + "❇️ Buy Price: "+ NumberList[2] + "\n" 
    for x in range(3,len(NumberList)):
      signal1 = signal1 + "\n☑️ Target " + str(x-2) + ": " + NumberList[x]
      signal2 = signal2 + "\n☑️ Target " + str(x-2) + ": " + NumberList[x]
    signal1 = signal1 + "\n\n⛔ Stop Loss: " + NumberList[0]
    signal2 = signal2 + "\n\n⛔ Stop Loss: " + NumberList[0]
    bot.send_message(message.chat.id, signal1) 
    bot.send_message(message.chat.id, signal2) 
    NumberList.clear()


bot.polling()
