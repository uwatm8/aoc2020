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
    a += tl + '.'

    if not tl:
        a += '_'

a += "."

groups = a.split('_')


for i in range(len(groups)):
    g = groups[i].replace(' ', '')

    nPeople = groups[i].count(".") - 1

    # dict is faster but meh
    questions = []
    questionsAnswered = {}

    for q in g:
        if not q in questions:
            questions.append(q)
            questionsAnswered[q] = 1
        else:
            questionsAnswered[q] += 1

    for question in questions:
        if questionsAnswered[question] == nPeople:
            c += 1

    print(len(questions))
print("answer: ", c)
