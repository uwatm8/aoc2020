filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nl = len(l)

c = 0


ins = []
val = []

print("a", nl)

for i in range(nl):
    tl = l[i]

    inst = tl.split(' ')[0]
    valt = tl.split(' ')[1]

    ins.append(inst)
    val.append(int(valt))


i = 0
t = 0

print(val)

visited = []

while i < len(ins) and t < 10000:
    print("c", c)
    print("i", i)

    if not i in visited:
        visited.append(i)
    else:
        break

    if ins[i] == "acc":
        c += val[i]

    if ins[i] == "jmp":
        i += val[i]
        continue

    i += 1
    t += 1

print("c", c)
