filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nl = len(l)

c = 0

nx = 3
ny = 1

for i in range(nl):
    tl = l[i]


print("answer: ", c)
