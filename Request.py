from allMessages import messages
from DuckDuckGo import DuckDuckGo
import time

class Request:
    def __init__(self, bot):
       self._bot = bot
       self._params = {"topic" : "", "filetype" : ["pdf"], "sites" : [], "max_results" : 5}
    def get_topic(self, msg):
        books = []
        self._params["topic"] = msg.text
        crawler = DuckDuckGo()
        print(self._params)
        books = crawler.get_books(self._params)
        for i in books:
            self._bot.send_message(msg.chat.id, i)
            time.sleep(1)
        self._bot.send_message(msg.chat.id, messages["finished_crawling"])
    def get_max_result(self, msg):
        if msg.text == "0":
            self._params["max_results"] = 5
        else:
            self._params["max_results"] = int(msg.text)
        self._bot.send_message(msg.chat.id, f"Done! I will now show a maximum of {self._params['max_results']} results")
    def get_filetypes(self, msg):
        if msg.text == "0":
            self._params["filetype"] = ["pdf"]
        else:
            self._params["filetype"] = msg.text.split(", ")
        self._bot.send_message(msg.chat.id, f"Done! From now on I'll only show {', '.join(self._params['filetype'])} formatted documents")
    def get_sites(self, msg):
        if msg.text == "0":
            self._params["sites"] == []
        else:
            self._params["sites"] = msg.text.split(", ")
        self._bot.send_message(msg.chat.id, f"Done! From now on I'll only show documents from these sources: {', '.join(self._params['sites'])}")