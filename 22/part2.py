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


p1Win = False

ans = 0

# return True = p1 won
def play(l,l2):
  i = 0
  seenPairs = []
  while len(l) > 0 and len(l2) >0 and i < 10000:

    if False:
      print('') 
      print('i ', i) 
      print("l1", l)
      print("l2", l2)

    i += 1
    p1 = l.pop(0)
    #?p1 = l[:len(l)-1]
    p2 = l2.pop(0)

    if p1 <= len(l) and p2 <= len(l2):
      sd1 = l[:p1]
      sd2 = l2[:p2]
      
      p1Won, d1, d2  = play(sd1, sd2)
    else:
      p1Won = p1 > p2


    key = str(l)+'.'+str(l2)
    if not key in seenPairs:
      seenPairs.append(key)
    else:
      l.append(p1)
      l.append(p2)
      return True, l, l2
 
    if p1Won:
      l.append(p1)
      l.append(p2)
    else:
      l2.append(p2)
      l2.append(p1)


  if len(l):
    return True, l, l2
  else: 
    return False, l, l2


p1Won, l, l2  = play(l, l2)

if p1Won:
  for i in range(len(l)):
      tl = l[i] * (len(l) - i)
      ans += tl
else:
  for i in range(len(l2)):
      tl = l2[i] * (len(l2) - i)
      ans += tl

print("answer: ", ans)
