filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nls = len(l)

c = 0

mask = 0
val = ""

out = 0

memory = {}

for i in range(nls):

    tl = l[i]

    if len(tl.split('mask')) > 1:
        # isa mask
        mask = tl.split('mask = ')[1]
    else:
        a = tl.split("mem[")[1].split(']')[0]
        oa = a
        val = bin(int(tl.split(' = ')[1]))
        ov = int(val, 2)
        sval = str(val)[2:]
        sa = str(bin(int(a)))[2:]

        addedZeros = 36 - len(sval)

        for i in range(addedZeros):
            sval = '0'+sval

        addedZeros = 36 - len(sa)
        for i in range(addedZeros):
            sa = '0'+sa

        newVal = ""

        for i in range(36):

            if mask[i] == 'X':
                newVal = newVal + 'X'
            elif mask[i] == '1':
                newVal = newVal + '1'
            elif mask[i] == '0':
                newVal = newVal + sa[i]

        xes = newVal.count('X')

        combos = []

        for i in range(2**xes):
            combos.append(str(bin(i))[2:])

        longest = len(combos[len(combos) - 1])

        for i in range(2**xes):
            combos[i] = '0'*(longest-len(combos[i])) + combos[i]

        adresses = []

        for c in combos:
            newValCopy = newVal
            for i in range(len(c)):
                newValCopy = newValCopy.replace('X', c[i], 1)
            adresses.append(newValCopy)

        for a in adresses:
            memory[int(a, 2)] = int(ov)


c = 0
for a in memory:
    c += int(memory[a])

print("answer: ", c)
