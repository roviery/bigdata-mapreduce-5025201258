import sys
from itertools import groupby

def mapfunc(w):
    cleanword = ''.join([i for i in w if i.isalpha()])
    return [cleanword,1]

def reducefunc(key, values):
    counts = [x[1] for x in values]
    return [key, sum(counts)]

with open("book.txt") as f:
    words=[word for line in f for word in line.split()]

map_result = map(mapfunc, words)
map_result_sorted = sorted (map_result, key = lambda x: x[0])
reduce_result = []
for k, g in groupby(map_result_sorted, key = lambda x: x[0]):
    reduce_result.append(reducefunc(k, list(g)))

print(reduce_result)