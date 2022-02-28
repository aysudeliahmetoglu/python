#Finding the root of a 2nd degree equation with one unknown
#equation = ax^2 + bx + c
#delta =b ** 2 - 4 * a * c
#first root =(- b - delta ** 0.5) / (2 * a)
#second root =(- b + delta ** 0.5) / (2 * a)
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
delta=b **2 - 4 * a * c
x1=(- b - delta ** 0.5) / (2 * a)
x2=(- b + delta ** 0.5) / (2 * a)
print("first root: {}\nSecond root: {}".format(x1,x2))
