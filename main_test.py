
import logging
import os
import telebot

# Ініціалізація логера
logging.basicConfig(level=logging.INFO)

# Токен з environment змінної
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# ID користувача
USER_ID = int(os.getenv("USER_ID"))

# Повідомлення для тесту
morning_messages = [
    """🎯 ТЕСТОВЕ ПОВІДОМЛЕННЯ — РАНОК
Глечик каже: встав! Цей бот не чекає ранку, щоб дати тобі копняка."""
]

evening_messages = [
    """🌙 ТЕСТОВЕ ПОВІДОМЛЕННЯ — ВЕЧІР
Глечик питає: що ти зробив сьогодні, крім того, що запустив бота?"""
]

def send_test_messages():
    try:
        bot.send_message(USER_ID, morning_messages[0])
        bot.send_message(USER_ID, evening_messages[0])
    except Exception as e:
        logging.error(f"Помилка надсилання повідомлення: {e}")

send_test_messages()
