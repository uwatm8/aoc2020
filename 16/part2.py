filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nls = len(l)

ans = 0

fields = {}

hasFields = False
newyt = False

mynums = []
nearbynums = []


def canBeIndex(i, n):
    key = list(fields.keys())[i]

    if (n >= fields[key]['min1'] and n <= fields[key]['max1']) or (n >= fields[key]['min2'] and n <= fields[key]['max2']):
        return True

    return False


def de(n):
    n = int(n)
    for f in fields:
        if f != None:
            if (n >= fields[f]['min1'] and n <= fields[f]['max1']) or (n >= fields[f]['min2'] and n <= fields[f]['max2']):
                return True
    return False


for i in range(nls):
    tl = l[i]

    if not hasFields:

        fn = tl.split(': ')[0]

        if not fn:
            hasFields = True
            continue

        min1 = int(tl.split(': ')[1].split(' or ')[0].split('-')[0])
        max1 = int(tl.split(': ')[1].split(' or ')[0].split('-')[1])
        min2 = int(tl.split(': ')[1].split(' or ')[1].split('-')[0])
        max2 = int(tl.split(': ')[1].split(' or ')[1].split('-')[1])

        fields[fn] = {'min1': min1, 'max1': max1, 'min2': min2, 'max2': max2}

        if False:
            print(min1)
            print(max1)
            print(min2)
            print(max2)
            print(" ")

        continue

    if i == len(fields) + 2:
        for n in tl.split(','):
            mynums.append(n)

    if i > len(fields) + 4:
        nums = []

        for n in tl.split(','):
            nums.append(int(n))

        nearbynums.append(nums)

    ts = tl.split(',')


rr = []

for nn in nearbynums:
    for n in nn:
        if(not de(n)):
            rr.append(nn)


for r in rr:
    nearbynums.remove(r)

indexes = []

columnCanBeField = []

for f in range(len(fields)):
    columnCanBeField.append({})
    for i in range(len(nearbynums[0])):
        if not i in columnCanBeField[f]:
            columnCanBeField[f][i] = True


def removekey(d, key):
    print(d)
    r = dict(d)
    del r[key]
    return r


for f in range(len(fields)):
    for nn in range(len(nearbynums)):
        for n in range(len(nearbynums[nn])):
            if canBeIndex(f, nearbynums[nn][n]):
                # print(canBeIndex(f, nearbynums[nn][n]))
                continue
            else:
                # print(canBeIndex(f, nearbynums[nn][n]))
                columnCanBeField[f][n] = False


def hasOnlyOne(d):
    t = 0
    for key in d.keys():
        if d[key]:
            t += 1

    return t == 1


def theOne(d):
    for i in range(len(d.keys())):
        key = list(d.keys())[i]
        if d[key]:
            return i


def prune(n):
    for f in range(len(fields)):
        columnCanBeField[f][n] = False


column = {}


for i in range(len(fields) + 3):
    for f in range(len(fields)):
        if hasOnlyOne(columnCanBeField[f]):
            to = theOne(columnCanBeField[f])

            column[list(fields.keys())[f]] = to

            for j in range(len(columnCanBeField[f])):
                prune(to)


ans = 1

for key in fields.keys():
    if key.count('departure'):
        ans *= int(mynums[column[key]])

print("answer: ", ans)
