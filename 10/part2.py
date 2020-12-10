from natsort import natsorted

filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

l.append(0)
l = natsorted(l)

l.append(int(l[len(l)-1]) + 3)

nls = len(l)

ones = 0
threes = 0

print(l)
print("meh")


maxSearch = nls - 1
removedCombos = []
canskip = []

for i in range(maxSearch):
    tl = int(l[i])
    nl = int(l[i+1])

    if tl - nl == -1:
        ones += 1

        if i > 0:
            pl = int(l[i-1])

            if nl - pl < 3:
                canskip.append(True)
            else:
                canskip.append(False)

    if tl - nl == -3:
        threes += 1

print(canskip)

canskip.append(False)

combs = 1

streak = 0
for cs in canskip:
    if cs == True:
        streak += 1
    else:
        mult = 2**streak

        if streak < 3:
            combs *= mult
        else:
            combs *= mult-1
        streak = 0

print("answer: ", combs)
