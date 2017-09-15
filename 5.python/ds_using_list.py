shoplist=['apple','mango','carrot','banana']

print(" I have", len(shoplist), "items to purchase")


print("Theses item are : "),
for item in shoplist:
          print(item)

print("I also have to buy rice")
shoplist.append("rice")
print("my shoplist is now", shoplist)

print("I will sort my list now")
shoplist.sort()
print(shoplist)

print("the first item I will buy is", shoplist[0])
olditem=shoplist[0]

print("i bought the ", olditem)

shoplist.remove(shoplist[0])

print("my shopping list is now", shoplist)