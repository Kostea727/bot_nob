import telebot
import random
import os
import requests




print(os.listdir('images'))

from config import TOKEN
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['coin'])
def send_coin(message):
    result = random.choice(["Орёл 🦅", "Решка 💰"])
    bot.reply_to(message, f"🪙 Монетка подброшена! Выпало: {result}")



def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(8) 
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')



@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)


@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")



@bot.message_handler(commands=['predict'])
def send_prediction(message):
    predictions = [
        "Да, но будь осторожен...",
        "Нет. И ты сам знаешь почему.",
        "Судьба благосклонна к тебе ✨",
        "Лучше подожди немного ⏳",
        "Кошка видит успех рядом с тобой 🐱 мау",
        "Скоро всё станет ясно 🔮",
        "Звёзды говорят 'да', но с условием...",
        "Сомнения — твои враги сегодня 🌀",
        "Ответ не ясен, попробуй позже 🌫️",
        "Определённо да! 💫"
    ]
    result = random.choice(predictions)
    bot.reply_to(message, f"🔮 Твоё предсказание:\n\n{result}")






@bot.message_handler(commands=['mem'])
def send_mem(message):
   img_name = random.choice(['mem1.jpeg', 'mem2.jpeg', 'mem3.jpeg', 'mem4.jpg', 'mem5.jpg', 'mem6.png', 'mem7.jpg']
)
   with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 




def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

    
@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)


@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "🛠 Вот что я умею:\n\n"
        "/start или /hello - Приветствие\n"
        "/coin - Подбросить монетку 🪙\n"
        "/pass - Сгенерировать пароль 🔑\n"
        "/heh [число] - Напечатать 'he' несколько раз 😆\n"
        "/bye - Попрощаться 👋\n"
        "/predict - Получить предсказание 🔮\n"
        "/mem - Отправить случайный мем 🖼️\n"
        "/duck - Отправить случайную утку 🦆\n"
        "/fox - Отправить случайную лису🦊\n"
        "/truth - правда дня🧠\n"
        "/help - Показать это сообщение 📜"
    
    )
    bot.reply_to(message, help_text)

def get_fox_image_url():
    url = 'https://randomfox.ca/floof/'
    
    res = requests.get(url)
    res.raise_for_status()
    data = res.json()
    return data['image']
    
        

@bot.message_handler(commands=['fox'])
def send_fox(message):
    image_url = get_fox_image_url()
    bot.send_photo(message.chat.id, image_url)


@bot.message_handler(commands=['truth'])
def send_truth(message):
    truths = [
        "😴 Утро — это заговор против человечества.",
        "📱 Проверить телефон 100 раз в день — это уже хобби.",
        "💸 Деньги не главное, но без них всё остальное не работает.",
        "🐱 Кошки не живут с людьми — это люди живут у кошек.",
        "☕ Кофе не решает проблемы, но делает тебя милее, пока ты их решаешь.",
        "💡 Прокрастинация — это искусство делать вид, что ты занят.",
        "😂 Смех продлевает жизнь, особенно если смеёшься над собой.",
        "💤 «Ещё 5 минут» — это самая большая ложь в истории.",
        "📚 Опыт — это когда ты уже сделал все ошибки, но всё равно идёшь дальше.",
        "🎭 Иногда притворяться, что всё под контролем — единственный способ сохранить контроль."
    ]
    truth = random.choice(truths)
    bot.reply_to(message, f"🧠 Правда дня:\n\n{truth}")
    


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)



bot.polling()
