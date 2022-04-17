#slice method
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])