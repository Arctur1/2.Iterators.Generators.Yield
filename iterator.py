import json

class Iterator:

    def __init__(self, path: str):
        self.file = open(path)
        self.jsonfile = json.load(self.file)
        self.url = 'https://en.wikipedia.org/wiki/'

    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        country = self.jsonfile[self.a]['name']['common'].replace(' ', '_')
        self.a += 1
        if not country or len(self.jsonfile) == self.a:
            self.file.close()
            raise StopIteration
        return self.url + country