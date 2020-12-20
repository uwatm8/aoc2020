filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nls = len(l)

ans = 0

ns = []
nn = []

for i in range(nls):
    tl = l[i]

    if '"' in tl:
        ns.append(tl[1])
        nn.append(i)


done = False

input = l[0]


def choices(s):

    c = []
    s1 = s.split('|')[0]
    s2 = s.split('|')[1]

    c.append(s1)
    c.append(s2)

    print("choices", c)


i = 0
while not done and i < 4:
    i += 1
    sps = input.split(' ')

    for s in sps:

        if s.isnumeric():
            inner = l[int(s)]  # .replace('|', '_', 1)
            print("inner", inner)
            if '|' in inner:
                input = input.replace(str(s), '( '+inner+' )', 1)
                # print("split: ", inner.split('|'))
            elif len(inner.replace('" "', '').replace('"', '')) == 1:
                input = input.replace(str(s), inner, 1)
            else:
                input = input.replace(str(s), '( '+inner+' )', 1)

    while '(' in input:
        #print("parenthesis", input)
        s = input.find('(')
        e = 0

        depth = 0
        for i in range(len(input) - s):
            c = input[i+s]

            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1

            if depth == 0:
                e = i+s
                break

        input = input.replace(input[s:e+1], str(solve(input[s+1:e])), 1)

input = input.replace('" "', '').replace('"', '')
print(input)

choices("( ab | ba )")

done = True


print("answer: ", ans)
