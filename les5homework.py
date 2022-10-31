# БУСИНКИ https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=1&id_topic=26&id_problem=144
# красная + белая + синия + красная/белая/синяя
n = int(input())
print(n + 1)
# ЖУРАВЛИКИ https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=1&id_topic=28&id_problem=150
# петя и сережа одинаковое кол-во, катя в 2 раза больше чем петя + сережа
# x = петя и сережа, x + x = петя + сержа. катя = 4x
# x + x + 4x = s(24)
# 6x = 24   x = 4 (петя и сережа) катя = 16
s = int(input())
x = s // 6
print(x, x*4, x)
# КАНЦЕЛЯРСКИЕ ТОВАРЫ https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=1&id_topic=28&id_problem=148
# x карандаш = 3руб, y ручки, z флом
# y = x(3) + 2  y = z - 7
# y = 5         5 = z - 7   z = 12
x, y, z = map(int, input().split())
print(x*3 + y*5 + z*12)
# ЭНИЯ  https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=1&id_topic=26&id_problem=145
# n=кол-во панелей a и b = длина и ширина *2 стороны панели
n, a ,b = map(int, input().split())
print(n*a*b*2)
# БАНДИТЫ https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=1&id_topic=26&id_problem=146
a, b = map(int, input().split())
s = a + b - 1
print(s - a, s - b)
