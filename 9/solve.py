filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nl = len(l)

c = 0

for j in range(25):
    pass


for k in range(nl):
    tl = int(l[k])
    sol = False

    lim = 25

    # if not k % 25:
    #print("k", k)

    if k > lim:
        for i in range(lim):
            for j in range(lim):
                n1 = int(l[k-i-1])
                n2 = int(l[k-j-1])

                if k >= lim and n1 + n2 == tl and n1 != n2:
                    sol = True
                    continue

        if not sol:
            print("sol", tl)
            break

print("answer: ", c)
