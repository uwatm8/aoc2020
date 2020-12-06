filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        line = fp.readline()
        l.append(line.strip())
        cnt += 1


for i in range(len(l)-1):
    for j in range(len(l)-1):
        n1 = int(l[i])
        n2 = int(l[j])
        if n1 + n2 == 2020:
            print("solution: ", n1 * n2)
