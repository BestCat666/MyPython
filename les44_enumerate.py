a = [10,20,30,40]
s = 'hello'
t = ('apple','banana')
 
print(list(enumerate(a)))
#[(0, 10), (1, 20), (2, 30), (3, 40)] по сути индексы
#for para in enumerate(a):
for index, value in enumerate(a):
    if value % 20 == 0:
        print(index, value)
for index, value in enumerate(s):
        print(index, value)

for index, value in enumerate(a):
    if value % 20 == 0:
        print(index, value)
for index, value in enumerate(range(10,20)):
        print(index, value)

for index, value in enumerate(t,10): 
        print(index, value)