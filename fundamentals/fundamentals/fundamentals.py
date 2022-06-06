"""
JS - Data types
numbers
boolean true/false
strings
null
undefined
"""

#This is a comment
grade = 8.8
age = 25

#Print in console.log("message here");
print(age)
print(type(age))
print(type(grade))

#booleans
flag = True
print(flag)

#Snake case naming convention - firstName
first_name = "Michael"
print(first_name)

middle_name = None
print(middle_name)

#Arrays in Python, or know as "lists"
numbers = [10,20,30,40,50]
print(numbers)

#To access specific part of list
print(numbers[0])

#To access list length
print("Length of numbers:", len(numbers))

print("Length of numbers: " + str(len(numbers)))

#Access list length and print within string
print(f"Length of numbers: {len(numbers)} {first_name} {age} {grade}")

#"\n" counts as a "enter key" to list remainder under the next line

#Tuple is a variable where items/valuies cannot be changed down the road
numbers[0] = 15
print(numbers)

numbers_tuple = (10,20,30,40,50)
print(numbers_tuple)

#add or remove an item/value from list, not possible with Tuple
numbers.append(60)
print(numbers)

numbers.pop(3)
print(numbers)