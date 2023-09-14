l=[1,2,3,1,4,5,3,5]
l.sort()
print (l)
y=(l[0])
print(y)
for i in l:
    if i != y:
        print(i)
        y=i


