# example
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total

x = 20
y = 30
result = add_two_numbers(x,y)

print(result)

def print_grades(grade1 = 0.0, grade2 = 0.0, grade3 = 0.0):
    print("Grade 1 ", grade1)
    print("Grade 2 ", grade2)
    print("Grade 3 ", grade3)

print_grades(grade3 = 8.8, grade2 = 9.2, grade1 = 7.4)

#debug practice
def some_function(list):
    total = 0
    for element in list:
        total += element
    return total

nums= [1,2,3,4,5,6,7,8,9,10]
total = some_function(nums)
print("Expecting a 55", f"Got a {total}")