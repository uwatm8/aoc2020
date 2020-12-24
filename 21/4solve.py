filepath = 'data1.txt'
filepath2 = 'data2.txt'

l = []
l2 = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()
nls = len(l)

with open(filepath2) as fp:
    line = fp.readline()
    while line:
        l2.append(line.strip())
        line = fp.readline()
nls = len(l)
nls2 = len(l2)

ans = 0

couldBeAlergy = {}
couldBeIngred = {}
allIngreds = []
allAlergy = []

for i in range(nls):
    tl = l[i]

    ingreds, alergies = tl.strip(')').split('(contains')

    ingreds = tl.split(' (contains')[0].split(" ")
    alergies = tl.split('(contains')[1].strip(')').strip(' ').split(',')

    for i in ingreds:
        if i not in allIngreds:
            allIngreds.append(i)

        if i not in couldBeAlergy:
            couldBeAlergy[i] = []

            for a in alergies:
                if not a in couldBeAlergy[i]:
                    couldBeAlergy[i].append(a)
        

            
        for cba in couldBeAlergy[i]:
            if cba not in alergies:
                print("removing", cba)
                couldBeAlergy[i].remove(cba)
                                    

    print("ingreds", ingreds)
    print("alergies", alergies)


print(" ")
print(couldBeAlergy)

for cba in couldBeAlergy:
    items = len(couldBeAlergy[cba])
    print(items)
    if items == 0:
      ans += 1


print("answer: ", ans)
