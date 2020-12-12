import math

filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nl = len(l)

x = 0
y = 0

dx = 1
dy = 0

fx = 1
fy = 0

angle = 90

dtr = 0.0174533

direction = 'E'

for i in range(nl):
    tl = l[i]

    direction = tl[:1]
    dist = int(tl[1:])

    if (direction == 'F'):
        x += dist * fx
        y += dist * fy

    if (direction == 'L'):
        fx = fy
        fy = fx

        angle -= dist

        fx = round(math.sin(angle*dtr))
        fy = round(math.cos(angle*dtr))

    if (direction == 'R'):

        angle += dist

        fx = round(math.sin(angle*dtr))
        fy = round(math.cos(angle*dtr))

    if (direction == 'N'):
        dx = 0
        dy = 1

        x += dist * dx
        y += dist * dy

    if (direction == 'E'):
        dx = 1
        dy = 0

        x += dist * dx
        y += dist * dy

    if (direction == 'S'):
        dx = 0
        dy = -1

        x += dist * dx
        y += dist * dy

    if (direction == 'W'):
        dx = -1
        dy = 0

        x += dist * dx
        y += dist * dy

print("answer: ", abs(x) + abs(y))
