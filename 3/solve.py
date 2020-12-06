filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        #print("Line {}: {}".format(cnt, line.strip()))
        l.append(line.strip())
        line = fp.readline()
        cnt += 1

nl = len(l)

c = 0

nx = 3
ny = 1


for i in range(nl):
    tl = l[i]
    lineLength = len(tl)

    if tl[(i*nx) % lineLength] == '#':
        c += 1

print("answer: ", c)
