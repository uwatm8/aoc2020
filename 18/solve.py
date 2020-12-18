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
    j = 0

    nums = []

    signs = []

    while '(' in text and j < 500:
        j += 1
        print("parenthesis", text)
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

        text = text.replace(text[s:e+1], str(solve(text[s+1:e])))

    print("TEXT", text)

    sum = 0
    chars = text.split(' ')
    print(chars)
    for j in range(len(chars)):
        if not j % 2:
            nums.append(chars[j])
        else:
            signs.append(chars[j])

    print(nums)
    print(signs)
    sum = nums[0]

    for i in range(len(signs)):
        sum = aa(sum, signs[i], nums[i+1])

    return sum


for i in range(nls):

    print("  ")
    print("  ")
    print("  ")
    tl = l[i]

    print(tl)

    ans += solve(tl)

print("answer: ", ans)
