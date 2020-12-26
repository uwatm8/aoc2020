import re
from natsort import natsorted

import sys

sys.setrecursionlimit(100000000)

filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nls = len(l)

filepath2 = 'data2.txt'

l2 = []

with open(filepath2) as fp:
    line = fp.readline()
    while line:
        l2.append(line.strip())
        line = fp.readline()

nls2 = len(l2)

ans = 0

ns = []
nn = []

l = natsorted(l)


for i in range(len(l)):
    line = l[i]
    l[i] = line.split(": ")[1]

done = False


def choices(s):

    c = []
    s1 = s.split('|')[0]
    s2 = s.split('|')[1]

    c.append(s1)
    c.append(s2)

    print("choices", c)


print("done with replace")


def contain(data, i, acc):

    input = l[i]

    if '"' in input(data[acc: acc+1]):
        acc += 1
        return acc


for i in range(nls2):
    tl = l2[i]

    if contain(tl, 0, 0):
        ans += 1


print("answer: ", ans)
