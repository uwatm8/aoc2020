import math

filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nl = len(l)

c = 0

x = 0
y = 0

dx = 1
dy = 0

fx = 1
fy = 0

angle = 0

dtr = 0.0174533

direction = 'E'

wx = 10
wy = 1

for i in range(nl):
    tl = l[i]

    direction = tl[:1]
    dist = int(tl[1:])

    if (direction == 'F'):
        x += dist * wx
        y += dist * wy

    if (direction == 'L'):
        wxn = wx * round(math.cos(dist*dtr)) - wy * \
            round(math.sin(dist*dtr))
        wyn = wy * round(math.cos(dist*dtr)) + wx * \
            round(math.sin(dist*dtr))

        wx = wxn
        wy = wyn

    if (direction == 'R'):
        wxn = wx * round(math.cos(-dist*dtr)) - wy * \
            round(math.sin(-dist*dtr))
        wyn = wy * round(math.cos(-dist*dtr)) + wx * \
            round(math.sin(-dist*dtr))

        wx = wxn
        wy = wyn

    if (direction == 'N'):
        wy += dist

    if (direction == 'E'):
        wx += dist

    if (direction == 'S'):
        wy -= dist

    if (direction == 'W'):
        wx -= dist

print("answer: ", abs(x) + abs(y))
