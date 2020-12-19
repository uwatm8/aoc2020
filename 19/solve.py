filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nls = len(l)

ans = 0

ns = []
nn = []

for i in range(nls):
    tl = l[i]

    if '"' in tl:
        ns.append(tl[1])
        nn.append(i)


done = False

input = l[0]


while not done:
    sps = input.split(' ')

    ss = input.split('|')

    if len(ss) > 1:
        print("ss", ss)

    for s in sps:
        print('s', s)

        if s == '|':
            print("split: ", )

        if s.isnumeric():
            inner = l[int(s)]  # .replace('|', '_', 1)
            input = input.replace(str(s), inner, 1)

    print(input)

    done = True

print(ns)
print(nn)

print("answer: ", ans)
