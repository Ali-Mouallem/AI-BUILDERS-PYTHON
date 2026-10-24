def my_function():
    print("Hello, World!")

my_function() #calling the function

temp1=22
celsius1=(temp1-32)*5/9
print(f"Temperature in Celsius: {celsius1}")


temp2=33
celsius2=(temp2-32)*5/9
print(f"Temperature in Celsius: {celsius2}")


temp3=55
celsius3=(temp3-32)*5/9
print(f"Temperature in Celsius: {celsius3}")


def fahrenheit_to_celsius(temp): 
    celsius=(temp-32)*5/9
    return celsius
print(f"Temperature in Celsius: {fahrenheit_to_celsius(22)}")
print(f"Temperature in Celsius: {fahrenheit_to_celsius(33)}")
print(f"Temperature in Celsius: {fahrenheit_to_celsius(55)}")

def my_name(name , age , country = "USA"):
    print(f"My name is {name}, I am {age} years old and I live in {country}.")

print(my_name("Lara", 23))