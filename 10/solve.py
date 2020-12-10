from natsort import natsorted

filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()


c = 0

l.append(0)
l = natsorted(l)

l.append(int(l[len(l)-1]) + 3)

nls = len(l)

ones = 0
threes = 0

print(l)
print("meh")

canskip = []

maxSearch = nls - 1

for i in range(maxSearch):
    tl = int(l[i])
    nl = int(l[i+1])

    if tl - nl == -1:
        ones += 1

        if i+3 < maxSearch:
            nnl = int(l[i+3])

    if tl - nl == -3:
        threes += 1

print("answer: ", (ones)*(threes))
print("answer: ", (ones), (threes))
