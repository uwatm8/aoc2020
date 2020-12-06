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

a = ""

for i in range(nl):
    tl = l[i]
    a += tl

    if not tl:
        a += '_'

passports = a.split("_")
needToHave = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


for i in range(len(passports)):
    pp = passports[i]
    matches = 0
    for need in needToHave:
        if need in pp:
            matches += 1
    if matches == 7:
        c += 1

print("answer: ", c)
