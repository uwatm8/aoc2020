import math

filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nl = len(l)

c = 0

bi = int(l[0])
ids = l[1].split(',')

closestId = -1
closest = 100000

for i in ids:

    if i != 'x':
        i = int(i)

        left = i - bi % i
        if left < closest:
            closest = left
            closestId = i

print("answer: ", closest * closestId)
