from select import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.chrome.options import Options
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')

k = 0
def checkout(selected_name,k,chat_id):
    driver = webdriver.Chrome(r'/root/chrome/chromedriver',chrome_options=chrome_options)
    #driver = webdriver.Chrome(r'C:/chromedriver.exe')
    driver.get("https://abs.rafflesmedical.com.sg/eroster/Account/Logout")
    print(driver.title)
    #login here
    driver.find_element_by_id("editorUserName").send_keys("HCA-91090053")
    driver.find_element_by_id("password").send_keys("098890ang")
    ddelement = Select(driver.find_element_by_id("ddlClusters"))
    ddelement.select_by_index('13')
    driver.find_element_by_css_selector(".btn.btn-info").click()
    #go to attendance list
    driver.find_element_by_link_text("Attendance").click()
    driver.find_element_by_link_text("Attendance List").click()
    ddsession = Select(driver.find_element_by_class_name("ddlSession"))
    ddsession.select_by_index(k)
    driver.find_element_by_id("btnSearch").click()
    time.sleep(3)
    
    for i in range(1,40):
        i = str(i)
        name = driver.find_element_by_xpath(f'//*[@id="AttendanceList"]/tbody/tr[{i}]/td[2]/p[1]').text
        print(name)
        if selected_name in name:
            try:
                id = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div[2]/form/div[1]/table/tbody/tr['+str(i)+']/td[2]/p[1]').text
                driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div[2]/form/div[1]/table/tbody/tr['+str(i)+']/td[2]/p[5]/button[1]').click()           
                alert_obj = driver.switch_to.alert
                alert_obj.accept()
                time.sleep(2)
                print("done")
                bot.sendMessage(chat_id,f"{id} Accepted")
                k = 0
                driver.quit()
                return
            except:
                1
            bot.sendMessage(chat_id,"error")
            
        
    bot.sendMessage(chat_id,"Not found")
    k = 0
    driver.quit()
def on_chat_message(msg):
    global k
    content_type, chat_type, chat_id = telepot.glance(msg)
    if all(x.isalpha() or x.isspace() for x in msg["text"]):
        bot.sendMessage(chat_id,"wait..")
        checkout(msg["text"],k,chat_id) 
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Check In AM', callback_data='1')],
        [InlineKeyboardButton(text='Check In PM', callback_data='2')],
    ])

    bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)
    


def on_callback_query(msg):
    
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)
    global k
    if query_data == '1':
        
        k = 1
        markup = ReplyKeyboardMarkup(one_time_keyboard = True,resize_keyboard = True,keyboard=[
        [KeyboardButton(text='Eugene Ang')],
        [KeyboardButton(text='Yvonne Teo')],
        [KeyboardButton(text='Ann Grace')],
        [KeyboardButton(text='Cindy')],
        ])
        bot.sendMessage(from_id,"Select name for AM", reply_markup=markup)
        
    elif query_data == '2':
        
        k = 2
        markup = ReplyKeyboardMarkup(one_time_keyboard = True,resize_keyboard = True,keyboard=[
        [KeyboardButton(text='Eugene Ang')],
        [KeyboardButton(text='Yvonne Teo')],
        [KeyboardButton(text='Ann Grace')],
        [KeyboardButton(text='Cindy')],
        ])
        bot.sendMessage(from_id,"Select name for PM", reply_markup=markup)

bot = telepot.Bot('5338942609:AAETHA0jyz76Ey-ZCMA9VDlAL2djeKIHG9U')
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
while(1):
    time.sleep(1)



