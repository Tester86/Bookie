from duckduckgo_search import ddg

class DuckDuckGo:
    def __init__(self):
        pass
    def get_books(self, params):
        books = []
        query = f"{params['topic']}"
        for i in params['filetype']:
            query += f" filetype:{i} OR"
        if params["sites"] != []:
            query = query.rsplit(" ", 1)[0]
        for g in params['sites']:
            query += f" site:{g} OR"
        query = query.rsplit(" ", 1)[0]
        print(query)
        for j in ddg(query, max_results=params["max_results"]):
            for jj in params['filetype']:
                if j["href"].endswith(jj):
                    books.append(j["href"])
        return books