import telebot
from allMessages import messages
from Request import Request

bot = telebot.TeleBot("1963800839:AAF33PMSYp4QzYTP0XaAuAp_wt5wsKv1Lt0")

@bot.message_handler(commands=["help", "start"])
def help(msg):
    bot.send_message(msg.chat.id, messages["help"])

@bot.message_handler(commands=["request"])
def init_request(msg):
    req = Request(bot)
    bot.send_message(msg.chat.id, messages["topic_prompt"])
    bot.register_next_step_handler(msg, req.get_topic)

bot.polling()