import re
from natsort import natsorted

import sys

sys.setrecursionlimit(100000000)

filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nls = len(l)

filepath2 = 'data2.txt'

l2 = []

with open(filepath2) as fp:
    line = fp.readline()
    while line:
        l2.append(line.strip())
        line = fp.readline()

nls2 = len(l2)

ans = 0

ns = []
nn = []

l = natsorted(l)


for i in range(len(l)):
    line = l[i]
    l[i] = line.split(": ")[1]

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
hadNumber = True

while not done and hadNumber:
    i += 1
    sps = input.split(' ')

    nums = 0

    fixed = {}

    for s in sps:
        if s.isnumeric() and s not in fixed:
            fixed[s] = True
            nums += 1
            inner = l[int(s)]  # .replace('|', '_', 1)
            # if '|' in inner:
            input = input.replace(str(s), ' ( '+inner+' ) ')
            # print("split: ", inner.split('|'))
            # elif len(inner.replace('" "', '').replace('"', '')) == 1:
            #    input = input.replace(str(s), inner, 1)
            # else:
            #    input = input.replace(str(s), ' ( '+inner+' ) ', 1).

    input = input.replace('  ', ' ').replace('"', '')
    input = input.replace('35', 'b').replace('43', 'a')

    if not nums:
        hadNumber = False

    input = input.replace('a a', 'aa').replace(
        'b b', 'bb').replace('a b', 'ab').replace('b a', 'ba')

    # print(input)
    print("i:", i, nums, len(input))

    input = input.replace('( ba | aa )', '(b|a)a')
    input = input.replace('( bb | ab )', '(b|a)b')
    input = input.replace('( ba | bb )', 'b(b|a)')
    input = input.replace('( aa | ab )', 'a(b|a)')

    input = input.replace('( aa )', 'aa')
    input = input.replace('( bb )', 'bb')
    input = input.replace('( ab )', 'ab')
    input = input.replace('( ba )', 'ba')

    input = input.replace('( b', '(b')
    input = input.replace('( a', '(a')
    input = input.replace('a )', 'a)')
    input = input.replace('b )', 'b)')

    input = input.replace('b (', 'b(')
    input = input.replace('a (', 'a(')
    input = input.replace(') a', ')a')
    input = input.replace(') b', ')b')

    input = input.replace('| b', '|b')
    input = input.replace('| a', '|a')
    input = input.replace('a |', 'a|')
    input = input.replace('b |', 'b|')

    input = input.replace(') |', ')|')
    input = input.replace('| (', '|(')

    input = input.replace(') )', '))')
    input = input.replace('( (', '((')
    input = input.replace(') (', ')(')

    #input = input.replace('a', '((')

    if False:
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

            #input = input.replace(input[s:e+1], str(solve(input[s+1:e])), 1)


#input = input.replace('( a ) ( a ) | ( a ) ( a )', 'aa')


# print(input)

print("done with replace")


if True:
    for i in range(nls2):
        "searching line"
        tl = l2[i]

        if '"' in tl:
            ns.append(tl[1])
            nn.append(i)

        reg = re.search(input, tl)
        if(reg and reg.group(0) == tl):
            ans += 1


print("answer: ", ans)
