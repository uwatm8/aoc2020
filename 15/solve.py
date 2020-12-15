filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nl = len(l)

c = 0

for i in range(nl):
    tl = l[i]

    ns = tl.split(',')

spoken = {}

spokenOrder = []

startingNums = len(ns)

for i in range(len(ns)):
    n = ns[i]
    print(n)

    spokenOrder.append(int(n))

for i in range(len(ns)-1):
    n = ns[i]

    spoken[n] = i

print("is", spoken)

iterations = 2020

print("a")

for i in range(iterations):
    if i == 0:
        continue

    if i < startingNums:
        continue

    lastSpoken = str(spokenOrder[i-1])

    if not lastSpoken in spoken:
        spokenOrder.append(0)
        spoken[str(lastSpoken)] = i - 1

        continue

    last = spoken[lastSpoken]+1

    diff = i - last

    spokenOrder.append(diff)

    spoken[str(lastSpoken)] = i - 1


# print(spokenOrder)
# print(spoken)

print("answer: ", spokenOrder[iterations-1])
