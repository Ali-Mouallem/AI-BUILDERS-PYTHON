set1={1,2,3,4,5}
print(type(set1))
print(len(set1))
print(set1)

set1.add(6)
print(set1)

fruit_set={'apple', 'banana', 'cherry','kiwi'}
set1.update(fruit_set)
print(set1)

set1.remove('banana')
print(set1)

# set1.remove('watermelon')
# print(f"Remove Result: {set1}") 

#discard
set1.discard('watermelon')
print(f"Discard Result: {set1}")

#pop
set1.pop()
print(f"Pop Result: {set1}")