filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nl = len(l)

c = 0

nx = 3
ny = 1

maxSeatId = -1

for i in range(nl):
    tl = str(l[i])

    rowPart = tl[:7]
    rowPart = rowPart.replace("B", "1").replace("F", "0")
    row = int(rowPart, 2)

    seatPart = tl[7:]

    seatPart = seatPart.replace("R", "1").replace("L", "0")
    seat = int(seatPart, 2)

    seatID = row * 8 + seat
    maxSeatId = max(seatID, maxSeatId)

print("answer: ", maxSeatId)
