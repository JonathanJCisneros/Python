"""
{
    name: "Alex"
}
"""

student = {
    "first_name": "Alex",
    "last_name": "Miller",
    "age": 25,
    "languages": ["JavaScript", "Python"]
}

#printing specific value within list
print(student["languages"][1])

l_n = "last_name"

print(l_n, student[l_n])

students= [{
    "first_name": "Alex",
    "last_name": "Miller",
    "age": 25
},
{
    "first_name": "Martha",
    "last_name": "Miller",
    "age": 22
}]

print(students[1]["first_name"], students[1][l_n])