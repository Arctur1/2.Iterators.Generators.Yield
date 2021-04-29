import json


class Myrange:

    def __init__(self, path: str):
        self.file = open(path)
        self.jsonfile = json.load(self.file)

    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        country = self.jsonfile[self.a]['name']['common']
        self.a += 1
        if not country or len(self.jsonfile) == self.a:
            self.file.close()
            raise StopIteration
        return country


if __name__ == '__main__':
    for countryname in Myrange('countries.json'):
        print(countryname)