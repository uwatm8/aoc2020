filepath = 'data.txt'

lines = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        lines.append(line.strip())
        line = fp.readline()

nl = len(lines)

changes = 1

l = []
newSeats = []

for x in range(len(lines)):
    l.append([])
    for y in range(len(lines[0])):
        l[x].append(lines[x][y])


iterations = 0

while changes > 0 and iterations < 200:
    changes = 0
    iterations += 1
    newSeats = []
    for x in range(nl):
        newSeats.append([])
        tl = l[x]

        for y in range(len(tl)):
            occupied = 0

            for xxx in range(3):
                for yyy in range(3):
                    yy = y - 1 + yyy
                    xx = x - 1 + xxx
                    if xx >= 0 and yy >= 0 and xx < nl and yy < len(tl) and not (x == xx and y == yy):
                        if l[xx][yy] == '#':
                            occupied += 1

            if l[x][y] == '.':
                newSeats[x].append('.')

            if l[x][y] == 'L':
                if occupied == 0:
                    newSeats[x].append('#')
                    changes += 1
                else:
                    newSeats[x].append('L')

            if l[x][y] == '#':
                if occupied >= 4:
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

print(iterations)

print("rows", len(l))

for i in range(len(l)):
    totalCount += l[i].count('#')

print("answer: ", totalCount)
