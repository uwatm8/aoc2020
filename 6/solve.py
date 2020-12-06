filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nl = len(l)

c = 0

a = ""

for i in range(nl):
    tl = l[i]
    a += tl + " "

    if not tl:
        a += '_'

groups = a.split('_')


for i in range(len(groups)):
    g = groups[i].replace(' ', '')

    # dict is faster but meh
    questions = []

    for q in g:
        if not q in questions:
            questions.append(q)

    c += len(questions)
    print(len(questions))


print("answer: ", c)
