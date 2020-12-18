filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nls = len(l)

ans = 0


lastWasNum = False


def aa(n1, sign, n2):
    if sign == "+":
        return int(n1)+int(n2)
    return int(n1)*int(n2)


def solve(text):

    nums = []

    signs = []

    #print("start:", text)

    while '(' in text:
        #print("parenthesis", text)
        s = text.find('(')
        e = 0

        depth = 0
        for i in range(len(text) - s):
            c = text[i+s]

            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1

            if depth == 0:
                e = i+s
                break

        text = text.replace(text[s:e+1], str(solve(text[s+1:e])), 1)

    #print("TEXT1", text)

    while '+' in text:
        s = text.find('+')
        n1 = text[:s]
        n2 = text[s+1:]  # .replace(' ', '_')

        n1s = n1.count(' ')

        n1n = n1.split(' ')[n1s-1]

        n2n = n2.split(' ')[1]  # .split(' ')

        #print("adnalskdn", n1n, '+', n2n)

        text = text.replace(str(n1n) + ' + ' + str(n2n),
                            str(aa(n1n, '+', n2n)), 1)

        #print("n1", n1, "aaaa", n1n)
        #print("n2", n2, "aaaa", n2n)

    #print("TEXT2", text)

    sum = 0
    chars = text.split(' ')
    # print(chars)
    for j in range(len(chars)):
        if not j % 2:
            nums.append(int(chars[j]))
        else:
            signs.append(chars[j])

    sum = nums[0]

    for i in range(len(signs)):
        sum = aa(sum, signs[i], nums[i+1])

    #print("sum", sum)
    return sum


for i in range(nls):

    #print("  ")
    #print("  ")
    tl = l[i]

    tans = int(solve(tl))

    print("i", i)
    print(tans)
    ans += tans
print(ans)

# 13976444272545
# 88501057856269

print("answer: ", ans)
