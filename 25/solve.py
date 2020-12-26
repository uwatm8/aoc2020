ans = 0

num = 1
subj = 7
div = 20201227

pubk1 = 9789649
pubk2 = 3647239
l1 = 0
l2 = 0

for i in range(30000000):

    num = num * subj
    num = num % div
    #print("subj", num, i+1)

    if num == pubk1:
        print("subj", num, i+1)
        l1 = i+1
        #subj = i+1
        print("i", i)
        break
num = 1

for i in range(30000000):

    num = num * subj
    num = num % div
    #print("subj", num, i+1)

    if num == pubk2:
        print("subj", num, i+1)
        l2 = i+1
        #subj = i+1
        print("i", i)

        break


def key(num, subj, l):
    for i in range(l):
        num = num * subj
        num = num % div
        #print("subj", num, i+1)
    return num


ans = key(1, pubk1, l2)

print("answer: ", ans)
