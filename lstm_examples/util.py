import csv
import numpy as np


def read_data(fname):
    with open(fname, 'r') as f:
        text, y = [], []
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            y.append(int(row[0]) - 1)
            text.append(row[2])
    return text, np.ravel(y)


class SymbolTable:
    """Wrapper for dict to encode unknown symbols"""

    def __init__(self, starting_symbol=2, unknown_symbol=1): 
        self.s       = starting_symbol
        self.unknown = unknown_symbol
        self.d       = dict()

    def lookup_add(self, w):
        if w not in self.d:
            self.d[w] = self.s
            self.s += 1
        return self.d[w]

    def lookup(self, w, strict=False):
        return self.d[w] if strict else self.d.get(w, self.unknown)

    def reverse(self):
        r = {v: k for k, v in self.d.iteritems()}
        r[0], r[1] = '~~NONE~~', '~~UNKNOWN~~'
        return r

    def num_words(self):
        return len(self.d)

    def num_symbols(self):
        return self.s