
ans = 0

input = "389125467"
iterations = 100

cups = []


def ca(cup, willBeRemoved):
    print("wwww", willBeRemoved)
    wbr = 0
    for i in range(len(cups)):
        if cups[i] in willBeRemoved:
            wbr += 1
            print("wbrrrrrrrrrrrrrrrrrrrrrrrrr", cups[i])
        if cup == cups[i]:
            return i

    return -1


for c in input:
    cups.append(int(c))

nls = len(cups)

for i in range(10):
    ii = i % nls
    # cups.remove(2)
    pickedVals = []
    print(" ")
    print("move ", i+1)
    print(cups)
    print("now ", cups[ii])
    for j in range(3):
        pickedVals.append(cups[(j+ii+1) % nls])

    selectedval = cups[ii] - 1

    if selectedval == 0:
        print("@@@@@@@@@@@@@@@@")
        selectedval = 9

    while selectedval in pickedVals:
        selectedval = ((nls + selectedval - 2) % nls) + 1

    #selectedval = ((nls+selectedval-2) % nls)+1

    w = ca(selectedval, pickedVals)
    print("w", w)
    print("selectedval", selectedval)
    #print("w", w)
    #print("w", (w + 1) % nls)
    print(pickedVals)

    for pv in pickedVals:
        cups.remove(pv)

    if w <= 0:
        print("extra", selectedval)
        cups.remove(selectedval)
        cups.append(selectedval)

    for j in range(3):
        insertIndex = (nls + w - 2 + j) % nls

        print("ii", insertIndex)

        cups.insert(insertIndex, pickedVals[j])


print(cups)
print("answer: ", ans)
