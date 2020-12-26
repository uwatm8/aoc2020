filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nl = len(l)

c = 0

subj = 7
div = 20201227

for i in range(10):
    print("subj", subj)

    subj *= subj
    subj %= div


for i in range(nl):
    tl = l[i]


print("answer: ", c)
