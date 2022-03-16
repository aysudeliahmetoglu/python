#Print the price entered from the keyboard on the screen by adding VAT (18%).

price=int(input("please enter price: "))

vat=price*18/100
new_price=vat+price
print("price with vat attached: ",new_price)