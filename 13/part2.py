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

bi = int(l[0])
ids = l[1].split(',')

closestId = -1
closest = 100000
smallestId = 10000

n = 1
fo = 0
o = False

multiplier = 1
additional = 0
found = 0
foundExtra = 0

iterations = 0

prevNumber = 1
while found + foundExtra < len(ids) - 1:
    iterations += 1
    a = False

    i = 0

    n1 = 0
    n2 = 0

    e1 = foundExtra
    e2 = foundExtra

    while i + found + foundExtra < len(ids):
        ii = ids[i+found + foundExtra]

        if ii == 'x':
            e1 += 1
            foundExtra += 1
            i -= 1

        else:
            n1 = int(ii)
            e1 += found
            found += 1
            break

        i += 1

    i = 0
    while i + found + foundExtra < len(ids):
        ii = ids[i+found + foundExtra]

        if ii == 'x':
            e2 += 1
            foundExtra += 1
            i -= 1
        else:
            n2 = int(ii)
            e2 += found
            break

        i += 1

    n = prevNumber

    if found + foundExtra == len(ids)-1:
        pass
        # last id : ids[len(ids)-1]

    while not a:
        if multiplier == 1:
            if (n+e1) % int(n1) == 0 and (n+e2) % int(n2) == 0:
                multiplier = n1*n2
                a = True
        else:
            if (n) % multiplier == prevNumber and (n+e2) % int(n2) == 0:

                multiplier *= n2
                a = True

        if a:
            prevNumber = n
            break

        n += multiplier
print("answer: ", n)
