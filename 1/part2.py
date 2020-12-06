filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        line = fp.readline()
        l.append(line.strip())
        cnt += 1

lines = len(l)-1

for i in range(lines):
    for j in range(lines):
        for k in range(lines):

            n1 = int(l[i])
            n2 = int(l[j])
            n3 = int(l[k])
            if n1 + n2 + n3 == 2020:
                print("solution: ", n1 * n2 * n3)
