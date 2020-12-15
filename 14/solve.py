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
        val = bin(int(tl.split(' = ')[1]))
        sval = str(val)[2:]

        addedZeros = 36 - len(sval)

        for i in range(addedZeros):
            sval = '0'+sval

        newVal = ""

        for i in range(36):

            if mask[i] == 'X':
                newVal = newVal + sval[i]
            else:
                newVal = newVal + mask[i]

        memory[a] = int(newVal, 2)

        print(" ")
        print(mask)
        print(sval)
        print(int(newVal, 2))


for a in memory:
    print(a)
    c += int(memory[a])

print("answer: ", c)
