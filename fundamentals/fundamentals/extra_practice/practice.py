# More Python Syntax practice since we only get 3 days to familiarize...

# #1
# print("Hello World")

# #2
# name = "Jonathan Cisneros"
# print("Hello", name)
# print("Hello " + name)

# #3
# name = 42
# print("Hello", name)
# print("Hello " + str(name))

# #4
# fave_food1 = "sushi"
# fave_food2 = "pizza"
# print("I love to eat {} and {}".format(fave_food1, fave_food2))
# print(f"I love to eat {fave_food1} and {fave_food2}")

# #5
# for i in range(151):
#     print(i)

# #6
# for i in range(5,1001):
#     if i % 5 == 0:
#         print(i)

# # OR

# for i in range(5,1001,5):
#     print(i)

# #7
# for i in range(1,101):
#     print(i)
#     if i % 10 == 0:
#         print("Coding Dojo")
#     if i % 5 == 0:
#         print("Coding")

# # 8
# final_sum = 0
# for i in range(500001):
#     if i % 2 == 1:
#         final_sum += i

# print(final_sum)

# # 9
# for i in range(2018, 0, -4):
#     print(i)

# # 10
# lowNum = 2
# highNum = 9
# mult = 3

# for i in range(lowNum, highNum + 1):
#     if i % mult == 0:
#         print(i)

# # 11
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())
# #  returns 5

# # 12
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# # Error

# # 13
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())

# #  returns only 5

# 14

# #4
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())
# #  returns 5

# # 15
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x)

# # print 5


# # 16
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))

# # pred. runs 8/ actual answer is 3 and 5 but issue with "+"

# # 17
# def concatenate(b,c):
#     return str(b)+str(c)
#     print(concatenate(2,5))

# # indent error, prints nothing unless "print" is back-spaced

# # 18
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(number_of_oceans_or_fingers_or_continents())

# # prints 100, then returns 10

# # 19
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

# #  prints 7, 14, 21

# # 20
# def addition(b,c):
#     return b+c
#     return 10
# print(addition(3,5))

# # print 8

# # 21
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
# print(b)
# foobar()
# print(b)

# # print 500, 500, 300, 500

# # 22
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)

# # prints 500, 500 300, 500

# # 23
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar()
# print(b)

# # prints 500, 500, 300, 300

# # 24
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()

# # prints 1,3,2

# # 25
# def foo():
#     print(1)
#     x = bar()
#     print(x)
#     return 10
# def bar():
#     print(3)
#     return 5
# y = foo()
# print(y)

# # prints 1,3,5,10

# # 26
# def countdown(num):
#     newStr = []
#     for i in range(num,-1, -1):
#         newStr.append(i)
#     return newStr

# print(countdown(7))

# # 27
# def print_and_return(list ):
#     print(list[0])
#     return list[1]

# print(print_and_return([1,2]))

# # 28
# def first_plus_length(list):
#     return list[0] + len(list)

# print(first_plus_length([1,2,3,4,5]))
