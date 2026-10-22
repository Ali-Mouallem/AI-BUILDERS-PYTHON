mylist = [1,2,2,3,4]
print (type(mylist))
print(mylist[2])

print(len(mylist))

mylist.append(10)
print(mylist)

mylist.remove(2)
print(mylist)

fruit_list=['apple', 'banana', 'cherry']
print(fruit_list)

mylist.extend(fruit_list)
print(mylist)

new_list=[x for x in fruit_list if "a" in x]
print(new_list)

ranging_list=[x for x in range(8)]
print(ranging_list)

print(ranging_list[0:5])
