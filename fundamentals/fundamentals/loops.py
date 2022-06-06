"""
Syntax does not exist within Python
for(var i=0; i<10; i++) {
    // Login inside loop
}
"""
#for loop in Python
for x in range(0,10):
    print(x)

#decrement for loop
for x in range(10,0,-1):
    print(x)

#increment by 2
for x in range(0,10,2):
    print(x)

#for loop an array
numbers = [10,20,30,40,50]

for x in range(0, len(numbers)):
    print(numbers[x])

#easier way to loop an array regardless of length
for num in numbers:
    print(num)

#loop through string
name = "Alexander"

for letter in name:
    print(letter)

print("First Letter: ", name[0])

#Access value within dictionary


students= {
    "first_name: ": "Alex",
    "last_name: ": "Miller",
    "age: ": 25,
    "languages: ": ["JavaScript", "Python"]
}

for key in students:
    print(key, students[key])

print("--------")

for language in students["languages: "]:
    print(language)

#While loop within Python
i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1