phrase="dont panic"
plist=list(phrase)
list3=["on tap"]
print(phrase)
print(plist)
new_phrase=list3[0]
for i in plist:
    plist=list3       
print(plist)

new_phrase=" ".join(plist)
print(new_phrase)