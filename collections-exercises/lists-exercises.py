mylist = [1,2,2,3,4]
print (type(mylist))
print(mylist[0])
print(len(mylist))
mylist.append(5)
print(mylist)
fruit_list = ['apple', 'banana', 'cherry']
print(fruit_list)
mylist.extend(fruit_list)
print(mylist)

new-list==[]
for x in fruit_list:
    if "a" in x:
        new-list.append(x)

print(new-list)

new-list == [x for x in fruit_list if "a" in x]