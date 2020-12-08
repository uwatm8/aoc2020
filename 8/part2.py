filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nl = len(l)

c = 0


inso = []
valo = []

print("a", nl)

for i in range(nl):
    tl = l[i]

    inst = tl.split(' ')[0]
    valt = tl.split(' ')[1]

    inso.append(inst)
    valo.append(int(valt))


# just trying both
for j in range(len(inso)):
    ins = inso.copy()
    val = valo.copy()

    if ins[j] == "jmp":
        ins[j] = "nop"

    broken = False

    visited = []

    i = 0
    t = 0
    c = 0

    while i < len(ins) and t < 100000:

        if not i in visited:
            visited.append(i)
        else:
            broken = True
            break

        if ins[i] == "acc":
            c += val[i]

        if ins[i] == "jmp":
            i += val[i]
            continue

        i += 1
        t += 1

    if not broken:
        print("not broken")
        break
    else:
        print("broken")


print("c", c)
