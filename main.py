import telebot
import random

# Токен твоего бота
bot = telebot.TeleBot("8248674215:AAGh_FemXIATiM2C3DulJJkR6GnbfV6UzQ4")

# -----------------------
# 💫 Команда: /coin — подбросить монетку
# -----------------------
@bot.message_handler(commands=['coin'])
def send_coin(message):
    result = random.choice(["Орёл 🦅", "Решка 💰"])
    bot.reply_to(message, f"🪙 Монетка подброшена! Выпало: {result}")


# -----------------------
# 🔐 Команда: /pass — сгенерировать пароль
# -----------------------
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(8)  # длина пароля
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")


# -----------------------
# 👋 Команда: /start или /hello — приветствие
# -----------------------
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')


# -----------------------
# 😂 Команда: /heh — повторить "he"
# -----------------------
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)


# -----------------------
# 👋 Команда: /bye — прощание
# -----------------------
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")


# -----------------------
# 🔮 Команда: /predict — предсказания
# -----------------------
@bot.message_handler(commands=['predict'])
def send_prediction(message):
    predictions = [
        "Да, но будь осторожен...",
        "Нет. И ты сам знаешь почему.",
        "Судьба благосклонна к тебе ✨",
        "Лучше подожди немного ⏳",
        "Кошка видит успех рядом с тобой 🐱",
        "Скоро всё станет ясно 🔮",
        "Звёзды говорят 'да', но с условием...",
        "Сомнения — твои враги сегодня 🌀",
        "Ответ не ясен, попробуй позже 🌫️",
        "Определённо да! 💫"
    ]
    result = random.choice(predictions)
    bot.reply_to(message, f"🔮 Твоё предсказание:\n\n{result}")


# -----------------------
# 📩 Эхо-ответ на любые другие сообщения
# -----------------------
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


# -----------------------
# 🚀 Запуск бота
# -----------------------
bot.polling()
