
from generator import LineEncoder
from iterator import Iterator

if __name__ == '__main__':
    for countryname in Iterator('countries.json'):
        print(countryname)
    print(list(LineEncoder.lineencode('text')))