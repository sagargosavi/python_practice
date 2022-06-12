from itertools import cycle

li = [0, 1, 2, 3,4]

l = []
licycle = cycle(li)
nextelem = next(licycle)
for i in li:
    
    thiselem, nextelem = nextelem, next(licycle)
    print(thiselem, nextelem)
    l.append((thiselem, nextelem))
print(l)

i = 0
while len(li) > i:
    print(li[i:i+2])
    i+=2