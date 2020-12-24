filepath = 'data1.txt'
filepath2 = 'data2.txt'

l = []
l2 = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()
nls = len(l)

with open(filepath2) as fp:
    line = fp.readline()
    while line:
        l2.append(line.strip())
        line = fp.readline()
nls = len(l)
nls2 = len(l2)

ans = 0

for i in range(nls):
    tl = l[i]


for i in range(nls2):
    tl = l2[i]


print("answer: ", ans)
