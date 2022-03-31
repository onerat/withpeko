def sum(*args):
    s = 0
    for i in args:
         s += i
    return s

print(sum(10, 11, 12, 13, 88, 100))