#just like strings

myvar = 60
mylist = [10, 20, 30, 40, 50]

print(mylist[0])
print(mylist[1:3])

mylist.append(myvar)  # append at end of list
print(mylist)

mylist.insert(3, myvar)  # insert at 0-base index location
print(mylist)

# remove last item by default if no argument, else remove by 0-base
item_removed = mylist.pop(2)
print(item_removed)  # returned from .pop()
print(mylist)  # list updated with removed item

mylist.reverse()
print(mylist)

mynewlist = [3, 6, 1, 7, 5, 2, 0, 4]
mynewlist.sort()
print(mynewlist)
