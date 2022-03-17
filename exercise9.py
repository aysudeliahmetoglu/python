#Write a program that calculates the selling price of a product by adding the tax rate and profit rate from the keyboard over the purchase price.

purchase_price=int(input("please enter purchase price: "))
tax_rate=int(input("please enter tax rate: "))
profit_rate=int(input("please enter profit rate: "))

selling_price=purchase_price+(purchase_price*tax_rate/100)+(purchase_price*profit_rate/100)
print("selling price of the product is " ,selling_price)
