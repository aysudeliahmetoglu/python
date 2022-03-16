#Print the price entered from the keyboard on the screen by adding VAT (18%).

price=int(input("please enter price: "))

kdv=price*18/100
new_price=kdv+price
print("price with vat attached: ",new_price)