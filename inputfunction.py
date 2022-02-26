#getting input from user
a=input("lütfen bir sayı giriniz: ")
print(a)
b=int(input("okul numaranızı girin: ")) #conversion data type.
print("öğrencinin okul numarası:",b)
isim=input("lütfen isminizi giriniz:")
print("isminiz ",isim)
# printing the sum of 3 numbers received from the user to the screen.
x=int(input("lütfen 1.sayıyı giriniz: "))
y=int(input("lütfen 2.sayıyı giriniz: "))
z=int(input("lütfen 3.sayıyı giriniz: "))
print("girilen 3 sayının toplamı :" ,x+y+z)
#if string is entered instead of int as input, user should be warned.
try:
    a=int(input("a:"))
    
except ValueError:
    print("lütfen inputu doğru formatta giriniz!")


