#dictionary: ordered , changeable , do not allow duplicates

my_dict={ "name" : "Ali",
         "age" : 25,
         #"age" : 30, # duplicate key will be ignored
}

print(my_dict)
print(type(my_dict))
print(len(my_dict)) # how many types of data in the dictionary

# Access
print(my_dict["name"])
print(my_dict["age"])

new_dict={ "name" : "Ali",
         "age" : 25,
         "colors" : ["red", "green", "blue"],
}
print(new_dict)

my_dict["name"]="Ahmad" # change the value of the key
print(my_dict)

my_dict.update({"age":30}) # change the value of the key
print(my_dict)

my_dict["city"]="Beirut" # add new key-value pair
print(my_dict)

my_dict.update({"name":"Mhmd","country":"Lebanon"}) # add new key-value pair
print(my_dict)

my_dict.pop("age") # remove key-value pair
print(my_dict)

del my_dict["city"] # remove key-value pair
print(my_dict)

my_dict.clear() # remove all key-value pairs
print(my_dict)