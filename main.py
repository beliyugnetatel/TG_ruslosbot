
import schedule
import telebot
from threading import Thread
from time import sleep
import requests
import json
import datetime
import time

TOKEN = "5685395407:AAG7V7FNYvTCWptxFMZqyXdJnsmFORvtZUE"

bot = telebot.TeleBot('5685395407:AAG7V7FNYvTCWptxFMZqyXdJnsmFORvtZUE')


today = datetime.date.today()
current_time = today.strftime("%d/%m/%Y")

some_id = 411537609
__chat_id = 0

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)



class TelegramBot():

    @bot.message_handler(commands = ['start'])
    @staticmethod
    def start(message):
        
        TelegramBot.__chat_id = message.chat.id
        los = requests.get('https://russianwarship.rip/api/v1/statistics/latest')
        my_json = json.loads(los.text)
        bot.send_message(chat_id=TelegramBot.__chat_id, text='-Привіт! Цей бот показує актуальні втрати окупанта кожен день!')
        
        bot.send_message(chat_id=TelegramBot.__chat_id, text = '-Втрати окупанта станом на  ' +  str(current_time) + '  💀')
        bot.send_message(chat_id=TelegramBot.__chat_id, text =
        '<b>-Особового складу:  ' +  str(my_json['data']['stats']['personnel_units']) + '  💀\n\n' 
            + '-Танків:  ' + str(my_json['data']['stats']['tanks']) + '  🚜\n\n'
            + '-Бойових броньованих машин:  ' + str(my_json['data']['stats']['armoured_fighting_vehicles']) + '  🛞\n\n'
            + '-Літаків:  ' + str(my_json['data']['stats']['planes']) + '  🛩\n\n'
            + '-Гелікоптериів:  ' + str(my_json['data']['stats']['helicopters']) + '  🚁\n\n'
            + '-Артилерійськіх систем:  ' + str(my_json['data']['stats']['artillery_systems']) + '  💣\n\n'
            + '-Одиниць РСЗВ:  ' + str(my_json['data']['stats']['mlrs']) + '  🧨\n\n'
            + '-Засобів ППО:  ' + str(my_json['data']['stats']['aa_warfare_systems']) + '  🕹\n\n'
            + '-БПЛА:  ' + str(my_json['data']['stats']['uav_systems']) + '  🛸\n\n'
            + '-Крилатих ракет:  ' + str(my_json['data']['stats']['cruise_missiles']) + '  🚀\n\n'
            + '-Кораблів/Катерів:  ' + str(my_json['data']['stats']['warships_cutters']) + '  🚢/🚤\n\n'
            + '-Автомобільної техніка та автоцистерни:  ' + str(my_json['data']['stats']['vehicles_fuel_tanks']) + '  🛞\n\n'
            + '-Спеціальної техніки:  ' + str(my_json['data']['stats']['special_military_equip']) + '  🛞 </b>\n\n',
            parse_mode='html')


    def function_to_run():
        los = requests.get('https://russianwarship.rip/api/v1/statistics/latest')
        my_json = json.loads(los.text)
        bot.send_message(chat_id=TelegramBot.__chat_id,text ='<b>-Втрати окупанта станом на  ' +  str(current_time) + '  💀</b>', parse_mode= 'html')
        bot.send_message(chat_id=TelegramBot.__chat_id, text =
        '<b>-Особового складу:  ' +  str(my_json['data']['stats']['personnel_units']) + '  💀\n\n' 
            + '-Танків:  ' + str(my_json['data']['stats']['tanks']) + '  🚜\n\n'
            + '-Бойових броньованих машин:  ' + str(my_json['data']['stats']['armoured_fighting_vehicles']) + '  🛞\n\n'
            + '-Літаків:  ' + str(my_json['data']['stats']['planes']) + '  🛩\n\n'
            + '-Гелікоптериів:  ' + str(my_json['data']['stats']['helicopters']) + '  🚁\n\n'
            + '-Артилерійськіх систем:  ' + str(my_json['data']['stats']['artillery_systems']) + '  💣\n\n'
            + '-Одиниць РСЗВ:  ' + str(my_json['data']['stats']['mlrs']) + '  🧨\n\n'
            + '-Засобів ППО:  ' + str(my_json['data']['stats']['aa_warfare_systems']) + '  🕹\n\n'
            + '-БПЛА:  ' + str(my_json['data']['stats']['uav_systems']) + '  🛸\n\n'
            + '-Крилатих ракет:  ' + str(my_json['data']['stats']['cruise_missiles']) + '  🚀\n\n'
            + '-Кораблів/Катерів:  ' + str(my_json['data']['stats']['warships_cutters']) + '  🚢/🚤\n\n'
            + '-Автомобільної техніка та автоцистерни:  ' + str(my_json['data']['stats']['vehicles_fuel_tanks']) + '  🛞\n\n'
            + '-Спеціальної техніки:  ' + str(my_json['data']['stats']['special_military_equip']) + '  🛞 </b>\n\n',
            parse_mode='html')

okl = TelegramBot()
okl.function_to_run()


if __name__ == "__main__":
        
    schedule.every().day.at("20:36").do(okl)
    Thread(target=schedule_checker).start() 

    bot.polling(none_stop=True, interval=0)

    
    