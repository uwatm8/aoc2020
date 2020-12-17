import math
filepath = 'data.txt'


l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nls = len(l)

ans = 0

size = 12

sx, bx, sy, by, bz, sz = 0, 0, 0, 0, 0, 0

current = {}

iterations = 6


def key(x, y, z, w):
    return str(x) + '.' + str(y) + '.' + str(z) + '.' + str(w)


for y in range(nls):
    tl = l[y]
    for x in range(len(tl)):
        current[key(x-1, y-1, 0, 0)] = tl[x] == '#'


def getVal(x, y, z, w, vals):
    k = key(x, y, z, w)

    if k in current:
        return current[k]
    else:
        return False


def tt(ax, ay, az, aw, vals):
    total = 0
    for ix in range(3):
        for iy in range(3):
            for iz in range(3):
                for iw in range(3):
                    x = ax + math.floor(ix - 1)
                    y = ay + math.floor(iy - 1)
                    z = az + math.floor(iz - 1)
                    w = aw + math.floor(iw - 1)

                    if getVal(x, y, z, w, current) and not (x == ax and y == ay and z == az and w == aw):
                        total += 1
    return total


for i in range(iterations):
    ni = {}
    print("iteration", i)
    print("size", len(current))
    size += 2
    for ix in range(size):
        x = math.floor(ix - (size-1)/2)
        #print("x", x)
        for iy in range(size):
            y = math.floor(iy - (size-1)/2)
            #print("y", y)
            for iz in range(size):
                z = math.floor(iz - (size-1)/2)
                for iw in range(size):
                    w = math.floor(iw - (size-1)/2)
                    #print("z", z)

                    t = tt(x, y, z, w, current)

                    k = key(x, y, z, w)

                    live = False
                    if k in current:
                        if current[k] and t == 2 or t == 3:
                            live = True

                    if t == 3:
                        live = True

                    ni[k] = live

    # print(ni)
    current = ni


print(tt(-1, -1, 0, 0, current))
print(len(current))


for f in current:
    if current[f]:
        ans += 1

print("answer: ", ans)
