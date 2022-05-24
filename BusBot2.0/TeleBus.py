from datetime import datetime
from datetime import timedelta
from aiohttp import ClientSession, ClientConnectorError
import requests
import urllib
from urllib.parse import urlparse
import json
import httplib2 as http
import sys
import os
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from math import cos, sqrt, pi
options = Options()

#driver = webdriver.Chrome(r'C:\Users\eugen\chromedriver.exe') #windows
#driver = webdriver.Chrome('/usr/bin/chromedriver')

#driver.get("http://trainarrivalweb.smrt.com.sg/")

R = 6371000 #radius of the Earth in m
def mrt(chat_id,k):

  try:
    driver.find_element_by_xpath(f"//*[@id='ddlStation']/option[contains(text(), '{k}')]").click()
    time.sleep(0.8)
    station = driver.find_element_by_xpath("/html/body/form/div[3]/div/div/div/div[2]/div[2]/span/div/table/tbody/tr[1]/td/p").text
    line = driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div/div[2]/div[2]/span/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/span[1]').text
    timing = driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div/div[2]/div[2]/span/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div[1]/table/tbody/tr[2]/td[1]').text
    ending = driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div/div[2]/div[2]/span/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div[1]/table/tbody/tr[3]/td[1]').text

    opptiming = driver.find_element_by_xpath("/html/body/form/div[3]/div/div/div/div[2]/div[2]/span/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div[2]/table/tbody/tr[2]/td[1]").text
    oppending = driver.find_element_by_xpath("/html/body/form/div[3]/div/div/div/div[2]/div[2]/span/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div[2]/table/tbody/tr[3]/td[1]").text
    message = f"""
Current Station: {station} @ {line}
==================================
Towards: {ending}
Next Train: {timing}
Towards: {oppending}
Next Train: {opptiming}
==================================
    """
    bot.sendMessage(chat_id,message)
    try:
      line2timing = driver.find_element_by_xpath("/html/body/form/div[3]/div/div/div/div[2]/div[2]/span/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div[3]/table/tbody/tr[2]/td[1]").text
      line2ending = driver.find_element_by_xpath("/html/body/form/div[3]/div/div/div/div[2]/div[2]/span/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div[3]/table/tbody/tr[3]/td[1]").text
      line2 = driver.find_element_by_xpath("/html/body/form/div[3]/div/div/div/div[2]/div[2]/span/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/span[10]").text
      line2timingopp = driver.find_element_by_xpath("/html/body/form/div[3]/div/div/div/div[2]/div[2]/span/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div[4]/table/tbody/tr[2]/td[1]").text
      line2endingopp = driver.find_element_by_xpath("/html/body/form/div[3]/div/div/div/div[2]/div[2]/span/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div[4]/table/tbody/tr[3]/td[1]").text
      message2 = f"""
Current Station: {station} @ {line2}
==================================
Towards: {line2ending}
Next Train: {line2timing}
Towards: {line2endingopp}
Next Train: {line2timingopp}
==================================
"""
      bot.sendMessage(chat_id,message2)

    except:
      1
  except:
    k == "exit"

def woodlands(chat_id):
  chrome_options = Options()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  driver = webdriver.Chrome(r'/root/chrome/chromedriver',chrome_options=chrome_options)
  driver.get("https://www.google.com/search?q=CIQ+to+woodlands&rlz=1C1KNTJ_enSG968SG968&oq=CIQ+to+woodlands&aqs=chrome..69i57j69i60l3.2806j0j9&sourceid=chrome&ie=UTF-8")
  time.sleep(1)
  print(driver.title)
  duration1 = driver.find_element_by_xpath("/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div[4]/div[3]/div/div/div[2]/div[1]/div[1]/div/div/span[1]/span[1]").text
  print(duration1)
  driver.get("https://www.google.com/search?q=woodlands+checkpoint+to+johor+CIQ&rlz=1C1KNTJ_enSG968SG968&ei=4EpyYsONBOSVseMPpbKv4Ao&ved=0ahUKEwjD_YW4x8X3AhXkSmwGHSXZC6wQ4dUDCA4&uact=5&oq=woodlands+checkpoint+to+johor+CIQ&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABMgUIIRCgATIFCCEQoAE6BwgAEEcQsAM6BwghEAoQoAE6BAghEBU6BggAEBYQHjoICCEQFhAdEB5KBAhBGABKBAhGGABQuQpYkiJgySRoAXABeACAAVaIAdUDkgEBOJgBAKABAcgBCMABAQ&sclient=gws-wiz")
  duration2 = driver.find_element_by_xpath("/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div[4]/div[3]/div/div/div[2]/div[1]/div[1]/div/div/span[1]/span[1]").text
  time.sleep(1)
  print(driver.title)
  message = f"""
Woodlands to CIQ: {duration1}
CIQ to Woodlands: {duration2}
  """
  bot.sendMessage(chat_id,message)
  driver.quit()
def Tuas(chat_id):
  chrome_options = Options()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  driver = webdriver.Chrome(r'/root/chrome/chromedriver',chrome_options=chrome_options)
  driver.get("https://www.google.com/search?q=Asia-Pacific+Brewery+to+Rest+%26+Service+Area+2nd+Link&rlz=1C1KNTJ_enSG968SG968&ei=21JyYuuHEY3bz7sPx-K82A4&ved=0ahUKEwir4amGz8X3AhWN7XMBHUcxD-sQ4dUDCA4&uact=5&oq=Asia-Pacific+Brewery+to+Rest+%26+Service+Area+2nd+Link&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsAM6BQghEKABOgQIIRAVSgQIQRgASgQIRhgAUD5Y4h5gjyFoAXAAeACAAXeIAbwEkgEDOC4xmAEAoAEBoAECyAEIwAEB&sclient=gws-wiz")
  time.sleep(1)
  print(driver.title)
  duration1 = driver.find_element_by_xpath("/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div[4]/div[3]/div/div/div[2]/div[1]/div[1]/div/div/span[1]/span[1]").text
  print(duration1)
  driver.get("https://www.google.com/search?q=Rest+%26+Service+Area+2nd+Link+to+Opp+Asia-Pacific+Brewery&rlz=1C1KNTJ_enSG968SG968&ei=kFJyYviEOdjAz7sP9JSF6AI&ved=0ahUKEwj4jPDizsX3AhVY4HMBHXRKAS0Q4dUDCA4&uact=5&oq=Rest+%26+Service+Area+2nd+Link+to+Opp+Asia-Pacific+Brewery&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsAM6BAghEBU6BQghEKABSgQIQRgASgQIRhgAUGFYshlgzBtoAXABeACAAcUBiAHYDZIBBDIzLjGYAQCgAQGgAQLIAQjAAQE&sclient=gws-wiz")
  duration2 = driver.find_element_by_xpath("/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div[4]/div[3]/div/div/div[2]/div[1]/div[1]/div/div/span[1]/span[1]").text
  time.sleep(1)
  print(driver.title)
  message = f"""
Tuas to Johor: {duration1}
Johor to Tuas: {duration2}
  """
  bot.sendMessage(chat_id,message)
  driver.quit()

def get(bus_stop):

  api_key = 'fmvxpJuBSEqtzoDSPGu/uw=='
  headers = { 'AccountKey' : api_key,'accept' : 'application/json'} #this is by default
  uri = 'http://datamall2.mytransport.sg/' #Resource URL
  path = f'ltaodataservice/BusArrivalv2?BusStopCode={bus_stop}' 
  target = urlparse(uri + path)
  #print (target.geturl())
  method = 'GET'
  body = ''
  h = http.Http()
  response,content = h.request(
      target.geturl(),
      method,
      body,
      headers)

  jsonObj = json.loads(content)
  #print(json.dumps(jsonObj, sort_keys=True, indent=4))
  
  with open(r"C:\Users\eugen\OneDrive\Codes\BusBot\bus_routes.json","w") as outfile:
      #Saving jsonObj["d"]
      json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)
  


def distance(lon1, lat1, lon2, lat2):
    x = (lon2 - lon1) * cos(0.5*(lat2+lat1))
    y = (lat2 - lat1)
    return (2*pi*R/360) * sqrt( x*x + y*y )



def out(i,data):

  try:
    
    service = data["Services"][i]["ServiceNo"]
    arrive = data["Services"][i]["NextBus"]["EstimatedArrival"]
    arrive2 = data["Services"][i]["NextBus2"]["EstimatedArrival"]
    load = data["Services"][i]["NextBus"]["Load"]
    load2 = data["Services"][i]["NextBus2"]["Load"]
    dest = data["Services"][i]["NextBus"]["DestinationCode"]
    bus_num = data["Services"][i]["ServiceNo"]
    size = data["Services"][i]["NextBus"]["Type"]
    size2 = data["Services"][i]["NextBus2"]["Type"]
    for j in range(0,12):
      try:
        #f = open(rf"C:\Users\eugen\OneDrive\Codes\BusBot\bus_stops{j}.json") #windows
        f = open(rf"bus_stops{j}.json")
        data = json.load(f)
        for k in range(0,500):
          try:  
            bus_stop_code = data["value"][k]["BusStopCode"]
            if(bus_stop_code == dest):
              term = (data["value"][k]["Description"])
              break
          except:
            1
      except:
        1
#    arrive3 = data["Services"][i]["NextBus3"]["EstimatedArrival"]
    arrived = arrive[11:16]
    arrived2 = arrive2[11:16]
#    arrived3 = arrive3[11:16]
    #current = datetime.now()
    current = datetime.now() + timedelta(hours = 8)
    current_time = current.strftime("%H:%M")
    
    FMT = '%H:%M'
#    tdelta3 = str(datetime.strptime(arrived3, FMT) - datetime.strptime(current_time, FMT))
    tdelta2 = str(datetime.strptime(arrived2, FMT) - datetime.strptime(current_time, FMT))
    tdelta = str(datetime.strptime(arrived, FMT) - datetime.strptime(current_time, FMT))
#    mins3 = tdelta2[2:4]
    mins2 = tdelta2[2:4]
    mins = tdelta[2:4]
    

    #print(current_time)
    
    if (mins == ' d'):
      mins = 'Delayed'
    elif mins == '00':
      mins = 'Arriving'
    else:
      mins = f'{mins} minutes'
    
    if (mins2 == ' d'):
      mins2 = 'Delayed'
    elif mins2 == '00':
      mins2 = 'Arriving'
    else:
      mins2 = f'{mins2} minutes'
    

#    if mins3 == ' d':
#      mins3 = 'Delayed'
#    elif mins3 == '00':
#      mins3 = 'Arriving'
#    else:
#      mins3 = f'{mins3} minutes'
    
    
    sentence = f"""
Service: {service} {term}
Arrival Time: {mins} Type: {size} Load: {load}
Arrival Time: {mins2} Type: {size2} Load: {load2} 
  
"""
    return sentence

   

  except:
     1
 
def handle(msg):
    
    content_type, chat_type, chat_id = telepot.glance(msg)
    #print(variable)	
    if content_type == 'text':
      variable = msg['text']
      if variable[0:1] == '/':
       variable = variable[1:]
       bot.sendMessage(chat_id,variable)
      else:
       bot.sendMessage(chat_id,variable)
#      if variable == 'stopbot':
#       driver.quit()
#       os._exit(0)
      
      if msg['text'] == '/start':
       markup = ReplyKeyboardMarkup(one_time_keyboard = True,resize_keyboard = True,keyboard=[
       [KeyboardButton(text='Bus Stop No.')],
       [KeyboardButton(text='Location',request_location=True)],
       [KeyboardButton(text='Singapore-Johor')],
       ])
       bot.sendMessage(chat_id, 'Seclect Option', reply_markup=markup)
          
      elif variable.isnumeric():
        bus_stop = variable
        print(bus_stop)

        
        for j in range(0,12):
          try:
            #f = open(rf"C:\Users\eugen\OneDrive\Codes\BusBot\bus_stops{j}.json") #windows
            f = open(rf"bus_stops{j}.json")
            data = json.load(f)

            for i in range(0,500):
              try:  
                bus_stop_code = data["value"][i]["BusStopCode"]
                if(bus_stop_code == bus_stop):
                  des = (data["value"][i]["Description"])

                  break


              except:
                1
          except:
            1
        namespace =f'Bus Stop: {bus_stop} {des} \n ==========================\n'
        get(bus_stop)
        f = open(r"C:\Users\eugen\OneDrive\Codes\BusBot\bus_routes.json") 
        data = json.load(f)
        for i in range(0,20):
          #out(i,data)
          if out(i,data) != None:
            namespace = namespace + out(i,data)
        namespace = namespace + "\nSEA (for Seats Available) \nSDA (for Standing Available) \nLSD (for Limited Standing)"
        bot.sendMessage(chat_id,format(namespace))
#      elif all(x.isalpha() or x.isspace() for x in variable):
#        station = variable[1:-3]
#        print(station)
#        mrt(chat_id,station)
      elif msg["text"] == 'Bus Stop No.':
        bot.sendMessage(chat_id,"Send me 5 Digit Bus Stop Code")
      elif msg["text"] == 'Singapore-Johor':
        bot.sendMessage(chat_id,"/Tuas or /Woodlands")
      elif variable == 'Woodlands':
        travel = """
Normal:0-30 mins
Heavy:30-60 mins
Severe: >60 mins
        """
        bot.sendMessage(chat_id,travel)
        woodlands(chat_id)
      elif variable == 'Tuas':
        travel = """
Normal:0-30 mins
Heavy:30-60 mins
Severe: >60 mins
        """
        bot.sendMessage(chat_id,travel)
        Tuas(chat_id)
      else:
        bot.sendMessage(chat_id,"I dont understand, press /start")
    elif content_type == 'location':
      dist =[]
      chat =''
      location = msg['location']
      lattitude = location["latitude"]
      longitude = location["longitude"]
      #print(lattitude)
      #print(longitude)
      for j in range(0,12):
        try:
          #f = open(rf"C:\Users\eugen\OneDrive\Codes\BusBot\bus_stops{j}.json") #windows
          f = open(rf"bus_stops{j}.json")
          data = json.load(f)
          for i in range(0,500):
            try:              
                lat = (data["value"][i]["Latitude"])
                log = (data["value"][i]["Longitude"])
                dista = distance(longitude,lattitude,log,lat)
                #print(f"{lat} {log}")
                stops = [dista,lat,log,i,j]
                dist.append(stops)                  
  
            except:
              1
        except:
          1
      sort = sorted(dist)
      #print(sort[0:5][0:5])
      for a in range(0,5):
        #k = open(rf"C:\Users\eugen\OneDrive\Codes\BusBot\bus_stops{sort[a][4]}.json")   #windows
        k = open(rf"bus_stops{sort[a][4]}.json")
        maped = json.load(k)
        nearest_stop = maped["value"][sort[a][3]]["Description"]
        distance_from = round(sort[a][0])
        nearest_stop_code = maped["value"][sort[a][3]]["BusStopCode"]
        
        message = f"""
Nearest Stop: {nearest_stop} 
Bus Stop Code: /{nearest_stop_code} 
Distance: {distance_from}m
"""
        chat = chat + message
      bot.sendMessage(chat_id,chat)
      
    else:
        bot.sendMessage(chat_id,"I dont understand")
        print("Null")
        

bot = telepot.Bot('5158422581:AAFsL5Iki3vb_RBRl_2KkIpY2wcSHNMNgf8')
MessageLoop(bot,handle).run_as_thread()
  
while 1:
  time.sleep(1)
