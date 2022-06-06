# x++,x--,=== doesn't exist

"""
* / %
+ -
< > >= <= != ==
and
or
=
"""

num = 20

if num == 10 or num == 20: 
    print("It is a 10 or 20")
    print("This is inside the if")
elif num < 10:
    print("It is lesser than 10")
else: 
    print("It's greater than 10")

print("This will always be printed")

