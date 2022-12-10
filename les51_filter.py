# def f(x):
#     if x > 10:
#         return True
#     else:
#         return False

def f(x):
    return x > 10

a = [14,15,0,19.45,46]
b = list(filter(f, a))
print(b)

a = ['ghbdjhf', 'ssd','sdjsdh']
b = list(filter(lambda x: len(x) > 4, a))
print(b)

a = "djhfskjhfGJHG454"
b = list(filter(str.isdigit, a))
c = list(filter(str.isalpha, a))
print(b)
print(c)