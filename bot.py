import telebot
from datetime import datetime

# Replace 'YOUR_API_TOKEN_HERE' with the token you received from BotFather
API_TOKEN = '6501902835:AAGmswts-7F3bt5V2fpoYRgGfG6RVkdpyI0'

# Initialize the bot
bot = telebot.TeleBot(API_TOKEN)

# Handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm your new Telegram bot. How can I assist you today?")

# Handle the /help command
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Here are some commands you can use:\n"
        "/start - Start interacting with the bot\n"
        "/time - Get the current time\n"
        "/echo - I will repeat whatever you say\n"
    )
    bot.reply_to(message, help_text)

# Handle the /time command to provide the current time
@bot.message_handler(commands=['time'])
def send_time(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bot.reply_to(message, f"The current time is: {now}")

# Handle the /echo command to repeat the user's message
@bot.message_handler(commands=['echo'])
def echo_message(message):
    text_to_echo = message.text[len('/echo '):]  # Remove the command part
    if text_to_echo.strip():  # Check if there is something to echo
        bot.reply_to(message, text_to_echo)
    else:
        bot.reply_to(message, "Please provide a message to echo.")

# Handle all other messages with a default reply
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, "I'm here to help! Use /help to see what I can do.")

# Start polling to check for new messages
if __name__ == "__main__":
    bot.polling()
