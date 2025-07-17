import telebot
import os
from flask import Flask # Yeh hum bot ko hamesha chalu rakhne ke liye use karenge
from threading import Thread

# Tumhara Telegram bot token
BOT_TOKEN = '7882537126:AAEBOGNN03dT4j1jZRjgl3p9tys6J6ZWtQI' 

# Bot object banate hain
bot = telebot.TeleBot(BOT_TOKEN)

# Yeh function /start command ko handle karega
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Namaste! Main tumhara naya bot hu. Main abhi test mode mein hu.")

# Bot ko hamesha chalu rakhne ke liye ek simple web server
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Bot is running."

def run_flask_app():
    # Pydroid 3 mein default port 8080 hota hai
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080)) 

# Bot polling ko ek alag thread mein chalate hain
def run_bot_polling():
    print("Bot chalne ke liye taiyar hai...")
    bot.polling(none_stop=True) # none_stop=True bot ko hamesha chalu rakhta hai

if __name__ == "__main__":
    # Flask app ko alag thread mein start karte hain
    flask_thread = Thread(target=run_flask_app)
    flask_thread.start()

    # Bot polling ko main thread mein start karte hain
    run_bot_polling()
