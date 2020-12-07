filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nl = len(l)

c = 0

bags = []
bagso = []
bagCanContain = {}
bagCanContaino = {}

for i in range(nl):

    # remove numbers too
    tl = l[i]

    tl = tl.replace('.', '')
    tl = tl.replace('bags', 'bag')
    tl = tl.replace('o other bags', '0 other bags')

    tlo = tl
    tl = ''.join(
        [i for i in tl if not i.isdigit()])

    bag = tl.split('contain')[0]
    bag = bag[:len(bag)-1]

    containing = tl.split('contain')[1]
    containingo = tlo.split('contain')[1]

    if ',' in containing:
        containing = containing.split(',')
    else:
        containing = [containing]

    if ',' in containingo:
        containingo = containingo.split(',')
    else:
        containingo = [containingo]

    if not bag in bags:
        # new bag
        bags.append(bag)
        bagCanContain[bag] = []
        bagCanContaino[bag] = []

    for contain in containing:
        if not 'o other bag' in contain:
            contain = contain[2:]
            bagCanContain[bag].append(contain)

    for containo in containingo:
        if not 'o other bag' in contain:
            containo = containo[1:]
            bagCanContaino[bag].append(containo)


print(bagCanContaino['shiny gold bag'])


children = bagCanContaino['shiny gold bag']

multi = 1


def getChildren(parent, total, multiplier):
    children = bagCanContaino[parent]

    totalChildren = 0
    for child in children:
        print("child", child)
        childKey = child[2:]
        childAmount = int(child[:1])
        totalChildren += childAmount
        total = getChildren(childKey, total, multiplier * childAmount)

    return total + totalChildren * multiplier


while children:
    for child in children:
        childKey = child[2:]

        print(childKey)

        childAmount = int(child[:1])

        multi *= childAmount

        c += len(children) * multi

        children = bagCanContaino[childKey]

        print(children)


print("ans2:", getChildren('shiny gold bag', 0, 1))

print("answer: ", c)
