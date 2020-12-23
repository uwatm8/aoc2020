filepath = 'data1.txt'
filepath2 = 'data2.txt'

l = []
l2 = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(int(line.strip()))
        line = fp.readline()
nls = len(l)

with open(filepath2) as fp:
    line = fp.readline()
    while line:
        l2.append(int(line.strip()))
        line = fp.readline()
nls = len(l)
nls2 = len(l2)

ans = 0
i = 0
while len(l) > 0 and len(l2) >0 and i < 10000:

  i += 1
  p1 = l.pop(0)
  #?p1 = l[:len(l)-1]
  p2 = l2.pop(0)
 
  if p1 > p2:
    l.append(p1)
    l.append(p2)

  if p2 > p1:
    l2.append(p2)
    l2.append(p1)


for i in range(len(l)):
    tl = l[i] * (len(l) - i)
    ans += tl

for i in range(len(l2)):
    tl = l2[i] * (len(l2) - i)
    ans += tl

print("answer: ", ans)
