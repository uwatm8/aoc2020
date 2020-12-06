filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        #print("Line {}: {}".format(cnt, line.strip()))
        line = fp.readline()
        l.append(line.strip())
        cnt += 1

nl = len(l)-1

for i in range(len(l)):
    print(l[i])
