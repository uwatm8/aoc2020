filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        #print("Line {}: {}".format(cnt, line.strip()))
        l.append(line.strip())
        line = fp.readline()
        cnt += 1

nl = len(l)


def trees(nx, ny):
    c = 0

    for i in range(nl):
        if i % ny == 0 and i != 0:
            tl = l[i]
            lineLength = len(tl)

            if tl[((i*nx)//ny) % lineLength] == '#':
                c += 1
    return c


print("answer: ", trees(1, 1) * trees(3, 1) *
      trees(5, 1) * trees(7, 1) * trees(1, 2))
