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

doesNotContain = {}

for i in range(nls):
    tl = l[i]

    ingreds, alergies = tl.strip(')').split('(contains')

    ingreds = tl.split(' (contains')[0].split(" ")
    alergies = tl.split('(contains')[1].strip(')').strip(' ').split(',')

    print(" ")
    print("i ", i)
    print("ingreds", ingreds)
    print("alergies", alergies)
    print(" ")


    for i in ingreds:
        if i not in allIngreds:
            allIngreds.append(i)

        if i not in couldBeAlergy:
            couldBeAlergy[i] = []
            doesNotContain[i] = []

        for a in alergies:
            if not a in couldBeAlergy[i]:
                if a not in doesNotContain[i]:
                    print("adding", a, "to", i)
                    couldBeAlergy[i].append(a.replace(" ", ""))
                else: 
                    print("does not contain")
    

        for cba in couldBeAlergy[i]:
            if cba not in alergies:
                #doesNotContain[i].append(cba.replace(" ", ''))
                print("removing", cba, "from", i)
                print(i, "does not contain", doesNotContain[i])
                #couldBeAlergy[i].remove(cba)
                                    

print(" ")
#print(couldBeAlergy)

print(" ")
print(" ")
print(" ")

for i in allIngreds:
    items = len(couldBeAlergy[i])
    print(i, couldBeAlergy[i], doesNotContain[i])
    if items == 0:
      ans += 1


print("answer: ", ans)
