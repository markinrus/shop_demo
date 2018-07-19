import requests
from tik import *

def get_bot_updates(limit, offset):
    url_t = url + token + '/getUpdates'
    par = {'limit': limit, 'offset': offset} 
    result = requests.get(url_t, params=par)
	
    decoded = result.json()
    return decoded['result']

def  sendmes_start(chat_id, text):
    url_t = url + token + '/sendMessage'
    par = {'chat_id': chat_id, 'text': text}
    result = requests.get(url_t, params=par)

# Получаем цену BTC в переменную btc_price
result_cript_btc = requests.get(url_cript_btc)
decoded_cript_btc= result_cript_btc.json()
btc_price = decoded_cript_btc['ticker']['price']

# Получаем цену BTC в переменную btc_price
result_cript_eth = requests.get(url_cript_eth)
decoded_cript_eth= result_cript_eth.json()
eth_price = decoded_cript_eth['ticker']['price']

# Получим только пять апдейтов
result = get_bot_updates(5, 0)
first_update = result[0]
text = result[0]['message']['text']
update_id = result[0]['update_id']


for item in result:
    text = item['message']['text']
    message_id = item['message']['message_id']
    update_id = item['update_id']
    chat_id = item['message']['chat']['id']

    if text == '/start':
        sendmes_start(chat_id, 'Приветствую! \nЧтобы узнать курсы криптовалют как:\n\n Биткоин - введите /btc \n\n Эфириум - введите /eth ')
    elif text == '/btc':
        sendmes_start(chat_id, ' Курс биткоина равен: ' + btc_price)
    elif text == '/eth':
        sendmes_start(chat_id, ' Курс эфириума равен: ' + eth_price)
    else:
        sendmes_start(chat_id, ' Не правильно введена команда! ')
    # отмечаем прочитанным
    
    new_offset = update_id + 1
    get_bot_updates(5, new_offset)
