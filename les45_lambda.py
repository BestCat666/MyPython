def f(x):
    return x**2
print(f(4))

#lambda arg1,arg2....:выражение
r = lambda x: x**2
print(r(7))


def perimetr(a,b,c):
    return a + b + c

per = lambda a, b, c: a + b + c

print(perimetr(1,2,3))
print(per(1,2,3))
h = lambda: 'hello'
print(h())

#сортировка по последней цифре!
a =[78,56,23,8,545,5000]
a.sort(key = lambda x: x%10)
print(a)

#сортировка по предпоследней цифре!
a =[78,56,23,8,545,5000]
a.sort(key = lambda x: x//10%10)
print(a)

def linear(k,b):
    return lambda x: x*k + b

graf1 = linear(2,5)
print(graf1(3))   # сюда уже принимает значение х


