from hashlib import md5

class LineEncoder:

    def lineencode(path):
        with open(path) as file:
            for line in file:
                yield md5(line.encode()).hexdigest()
