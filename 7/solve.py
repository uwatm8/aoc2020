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
bagCanContain = {}

for i in range(nl):

    # remove numbers too
    tl = l[i]
    tl = ''.join(
        [i for i in tl if not i.isdigit()])

    tl = tl.replace('.', '')
    tl = tl.replace('bags', 'bag')

    bag = tl.split('contain')[0]
    bag = bag[:len(bag)-1]

    containing = tl.split('contain')[1]

    if ',' in containing:
        containing = containing.split(',')
    else:
        containing = [containing]

    if not bag in bags:
        # new bag
        bags.append(bag)
        bagCanContain[bag] = []

    for contain in containing:
        if not 'o other bag' in contain:
            contain = contain[2:]
            bagCanContain[bag].append(contain)

for i in range(2):
    for bag in bags:
        for b in bagCanContain[bag]:
            newItems = []
            for newItem in bagCanContain[b]:
                if not newItem in bagCanContain[bag]:
                    newItems.append(newItem)
            # print("adding", newItem)

            for newItem in newItems:
                bagCanContain[bag].append(newItem)

for bag in bags:
    if 'shiny gold bag' in bagCanContain[bag]:
        c += 1

print("answer: ", c)
