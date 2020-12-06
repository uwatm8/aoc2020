filepath = 'data.txt'

lines = []

with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        #print("Line {}: {}".format(cnt, line.strip()))
        line = fp.readline()
        lines.append(line.strip())
        cnt += 1

t = 0

for i in range(len(lines)-1):
    line = lines[i]

    sp = line.split('-')
    mi = sp[0]
    ma = sp[1].split(' ')[0]

    letter = sp[1].split(' ')[1].split(':')[0]
    password = line.split(':')[1][1:]

    print("\n", line)
    print(letter)
    print(mi)
    print(ma)
    print(password)

    c = password.count(letter)

    if(c >= int(mi) and c <= int(ma)):
        t += 1

print("count", t)
