a = [5, 6, 7, 8]
b = [100, 200, 300, 400]

for i in range(4):
    print(a[i], b[i])

#rez = zip(a, b)
#print(list(rez))
#[(5, 100), (6, 200), (7, 300), (8, 400)]

rez = list(zip(a,b))
print(rez)

c = 'abcd'
rez2 = list(zip(a,b,c))
print(rez2)
col1, col2, col3 = zip(*rez2)
print(col1, col2, col3)
