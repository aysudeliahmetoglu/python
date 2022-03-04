#range(0,20) -Creates a sequence of numbers from 0 to 20.-

print(*range(0,20))  # * is prefixed to print.
print(*range(1,100,2))  #Prints from 1 to 100 in increments of 2.
print(*range(20,0,-1))
for i in range(0,20):
    print(i)

for i in range(0,10):
    print("* "*i)      #shape with stars