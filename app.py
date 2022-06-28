import telebot
from config import keys , TOKEN
from extensions import ConvertionExeptin,Convertor


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start','help'])
def heip(message:telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате : \n<имя валюты> \
<в какую валюту перевести > \
<количество переводимой валюты>\n список всех доступных валют : /valeus'
    bot.reply_to(message, text)

@bot.message_handler(commands=['valeus'])
def valeus(message:telebot.types.Message):
    text = 'Доступные валюты :'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def content(message: telebot.types.Message):
    try:
        valeus = message.text.split(' ')
        if len(valeus) != 3:
            raise ConvertionExeptin('Слишком много пораметров.')

        quote, base, amount = valeus

        total_base = Convertor.conver(quote, base, amount,)
    except ConvertionExeptin as e:
        bot.reply_to(message,f'Ощибка пользователя \n {e} ')
    except Exception as e:
        bot.reply_to(message,f'не удалось обратботать команду \n {e} ')
    else:
        text = f'Цена {amount} {quote} в {base} : {float(total_base) * float(amount)}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)

