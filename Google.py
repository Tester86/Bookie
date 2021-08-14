from googlesearch import search

class Google:
    def __init__(self):
        pass
    def get_books(self, params):
        books = []
        query = f"books {params['topic']}"
        for i in params['filetype']:
            query += f" filetype:{i} OR"
        if params["sites"] != []:
            query = query.rsplit(" ", 1)[0]
        for g in params['sites']:
            query += f" site:{g} OR"
        query = query.rsplit(" ", 1)[0]
        #DEBUG QUERY: print(query)
        for j in search(query, num=params['num'], stop=params['stop'], pause=params['pause']):
            for jj in params['filetype']:
                if j.endswith(jj):
                    books.append(j)
        return books