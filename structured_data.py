#Dictionaries

person = {'Name':'Ford Prefect','Gender':'Male','Occupation':'Researcher',
'Home Planet':'Betelgeus Seven'}
print(person)
print(person['Name'])
person['Age'] = 33
print(person)

found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0
print(found)
found['e'] += 1 
print(found)

# for k in found:
#     print(k,'was found',found[k],'time(s).')
for k in sorted(found):
    print(k,'was found',found[k],'time(s).')

