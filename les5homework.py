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
