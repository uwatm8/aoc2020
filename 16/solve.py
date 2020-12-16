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


for nn in nearbynums:
    for n in nn:
        if(not de(n)):
            print(n)
            ans += n

for i in range(len(fields)):
    pass

print("answer: ", ans)
