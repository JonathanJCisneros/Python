num1 = 42 #variable declaration, number

num2 = 2.3 #variable declaration, number

boolean = True #Boolean

string = 'Hello World' #string

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, array of strings

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary

fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, list of values as strings

print(type(fruit)) #log type of value

print(pizza_toppings[1]) #log statement, access value within variable

pizza_toppings.append('Mushrooms') #add value

print(person['name']) #log statement, access value

person['name'] = 'George' #initialize value

person['eye_color'] = 'blue' #initialize value

print(fruit[2]) #log statement, access value within array

if num1 > 45:
    print("It's greater") #if statement variable, log statement 
else:
    print("It's lower") #else statement, log statement

if len(string) < 5:
    print("It's a short word!") #if statement, length of string
elif len(string) > 15:
    print("It's a long word!") #else if statement, variable with string, log statement
else:
    print("Just right!") #else statement, log statement


for x in range(5):
    print(x) #for loop 0 < 5, log statement

for x in range(2,5):
    print(x) #for loop, between 2 < 5, log statement

for x in range(2,10,3):
    print(x) #for loop, 2 < 10, increment of 3, log variable

x = 0
while(x < 5):
    print(x)
    x += 1 #white loop, range between 0 and 5, log statement, increment by 1

pizza_toppings.pop() #remove value at end of string
pizza_toppings.pop(1) #remove value at 

print(person) #print values within dictionary
person.pop('eye_color') #remove key within variable
print(person) #print updated dictionary

for topping in pizza_toppings: #for loop regarding specific key in dictionary
    if topping == 'Pepperoni':
        continue #if statement allows loop to continue
    print('After 1st if statement') #log statement
    if topping == 'Olives':
        break #if statement breaking

def print_hello_ten_times(): #function with for loop, log statement 
    for num in range(10):
        print('Hello')

print_hello_ten_times() #function called

def print_hello_x_times(x): #function with for loop, log statement
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #function called with value

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #call function with original statemment
print_hello_x_or_ten_times(4) #calls function with new range


"""
Bonus section
"""

# print(num3) #print variable
# num3 = 72 #initalizing variable
# fruit[0] = 'cranberry' #changine value within array
# print(person['favorite_team']) #printing value of key within "person"
# print(pizza_toppings[7]) #print index '7' of pizza_toppings list
# print(boolean) #error, boolean undefined
# fruit.append('raspberry')  #add value to end of list
# fruit.pop(1) #remove index 1 of list