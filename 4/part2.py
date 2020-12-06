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
    a += tl + " "

    if not tl:
        a += '_'

passports = a.split("_")
needToHave = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def getVal(key, s):
    return s.split(key)[1].split(':')[1].split(' ')[0]


for i in range(len(passports)):

    print(i)

    pp = passports[i]
    matches = 0
    print(pp)

    if 'byr' in pp:
        v = int(getVal('byr', pp))
        if v >= 1920 and v <= 2002:
            matches += 1

    if 'iyr' in pp:
        v = int(getVal('iyr', pp))
        if v >= 2010 and v <= 2020:
            matches += 1

    if 'eyr' in pp:
        v = int(getVal('eyr', pp))
        if v >= 2020 and v <= 2030:
            matches += 1

    if 'hgt' in pp:
        v = getVal('hgt', pp)
        if 'cm' in v:
            hgt = int(v.split('cm')[0])
            if hgt >= 150 and hgt <= 193:
                matches += 1
        elif 'in' in v:
            hgt = int(v.split('in')[0])
            if hgt >= 59 and hgt <= 76:
                matches += 1

    print("matches", matches)
    if 'hcl' in pp:
        v = getVal('hcl', pp)

        hexes = 0
        if len(v) == 7:
            if v[0] == '#':
                for i in range(6):
                    try:
                        int(v[i+1], 16)
                        hexes += 1
                    except:
                        break

        if hexes == 6:
            matches += 1
    print("matches", matches)
    possibleEcl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if 'ecl' in pp:
        v = getVal('ecl', pp)

        if v in possibleEcl:
            matches += 1

    if 'pid' in pp:
        v = getVal('pid', pp)
        if len(v) == 9:
            try:
                int(v)
                matches += 1
            except:
                break

    if matches == 7:
        c += 1


print("answer: ", c)
