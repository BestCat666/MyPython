#[выражение for val in колеекция]
import random
lst = [0 for i in range(7)]
print(lst)
#[0, 0, 0, 0, 0, 0, 0]

lst2 = [i**2 for i in range(9)] 
print(lst2)
#[0, 1, 4, 9, 16, 25, 36, 49, 64]

lst3 = [i for i in 'hello']
print(lst3)
#['h', 'e', 'l', 'l', 'o']

a = [random.randint(-10,10) for i in range(9)]
print(a)
b = [abs(elem) for elem in a]
print(b)
c = [elem + 1 for elem in a]
print(c)

lst = [1,3,4,5,6,7,8,9,10] 
lst2 = [i for i in lst if i % 2 == 0]
print(lst2)

p = input().split()
p = [int(i) for i in p]
print(p)

n = 5
m = 4
a = [[0]*m for i in range(n)]
print(a)
for i in a:
    print(i)


list_ = [(i,j) for i in 'abc' for j in [1,2,3]]
print(list_)

