from allMessages import messages
from Google import Google
import tempfile
import urllib.request
import time

class Request:
    def __init__(self, bot):
       self._bot = bot
       self._params = {"topic" : "", "filetype" : ["pdf"], "sites" : [], "num" : 10, "stop" : 10, "pause" : 3}
    def get_topic(self, msg):
        self._params["topic"] = msg.text
        self._bot.send_message(msg.chat.id, messages["filetype_prompt"])
        self._bot.register_next_step_handler(msg, self.get_filetype)
    def get_filetype(self, msg):
        if msg.text != "0":
            self._params["filetype"] = msg.text.split(", ")
            print(self._params["filetype"])
        self._bot.send_message(msg.chat.id, messages["sites_prompt"])
        self._bot.register_next_step_handler(msg, self.get_sites)
    def get_sites(self, msg):
        if msg.text != "0":
            self._params["sites"] = msg.text.split(", ")
            print(self._params["sites"], end="\n\n")
        crawler = Google()
        books = crawler.get_books(self._params)
        for i in books:
            self._bot.send_message(msg.chat.id, i)
            time.sleep(2)