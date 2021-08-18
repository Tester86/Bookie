import telebot
from allMessages import messages
from Request import Request

bot = telebot.TeleBot("1963800839:AAF33PMSYp4QzYTP0XaAuAp_wt5wsKv1Lt0")
req = Request(bot)

@bot.message_handler(commands=["help", "start"])
def help(msg):
    bot.send_message(msg.chat.id, messages["help"])

@bot.message_handler(commands=["request"])
def init_request(msg):
    bot.send_message(msg.chat.id, messages["topic_prompt"])
    bot.register_next_step_handler(msg, req.get_topic)

@bot.message_handler(commands=["set_max_results"])
def set_max_results(msg):
    bot.send_message(msg.chat.id, messages["set_max_results"])
    bot.register_next_step_handler(msg, req.get_max_result)

@bot.message_handler(commands=["set_filetypes"])
def set_filetypes(msg):
    bot.send_message(msg.chat.id, messages["set_filetypes"])
    bot.register_next_step_handler(msg, req.get_filetypes)

@bot.message_handler(commands=["set_sites"])
def set_sites(msg):
    bot.send_message(msg.chat.id, messages["set_sites"])
    bot.register_next_step_handler(msg, req.get_sites)

bot.polling()