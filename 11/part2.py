filepath = 'data.txt'

lines = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        lines.append(line.strip())
        line = fp.readline()

nl = len(lines)
nc = len(lines[0])


l = []
newSeats = []

for x in range(len(lines)):
    l.append([])
    for y in range(len(lines[0])):
        l[x].append(lines[x][y])


def getSeatValue(dx, dy, x, y, seats):
    yy = y + dy
    xx = x + dx

    while xx >= 0 and yy >= 0 and xx < nl and yy < nc and not (x == xx and y == yy):
        if seats[xx][yy] != '.':
            return seats[xx][yy]

        yy = yy + dy
        xx = xx + dx

    return '.'


iterations = 0
changes = 1

while changes > 0 and iterations < 200:
    changes = 0
    iterations += 1
    newSeats = []
    for x in range(nl):
        newSeats.append([])
        tl = l[x]

        adjacent = 0

        for y in range(len(tl)):

            if l[x][y] == '.':
                newSeats[x].append('.')
            else:
                occupied = 0

                searched = 0

                values = []

                values.append(getSeatValue(1, 1, x, y, l))
                values.append(getSeatValue(0, 1, x, y, l))
                values.append(getSeatValue(-1, 1, x, y, l))
                values.append(getSeatValue(1, 0, x, y, l))
                values.append(getSeatValue(-1, 0, x, y, l))
                values.append(getSeatValue(1, -1, x, y, l))
                values.append(getSeatValue(0, -1, x, y, l))
                values.append(getSeatValue(-1, -1, x, y, l))

                occupied = values.count('#')

                # print(occupied)

                if l[x][y] == 'L':
                    if occupied == 0:
                        newSeats[x].append('#')
                        changes += 1
                    else:
                        newSeats[x].append('L')

                if l[x][y] == '#':
                    if occupied >= 5:
                        newSeats[x].append('L')
                        changes += 1
                    else:
                        newSeats[x].append('#')

    if False:
        print("new")
        for i in range(len(newSeats)):
            print(newSeats[i])

        print("old")
        for i in range(len(newSeats)):
            print(l[i])

        print(" ")
        print(" ")
        print(" ")
        print(" ")

    l = newSeats

totalCount = 0

print("iterations: ", iterations)

for i in range(len(l)):
    totalCount += l[i].count('#')

print("answer: ", totalCount)
