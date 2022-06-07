# 1. Countdown

arr = []

def countDown(num):
    for x in range(num, -1, -1):
        arr.append(x)

countDown(5)
print(arr)

# 2. Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))


# 3. First plus length
def first_plus_length(arr):
    print(arr[0], len(arr))

first_plus_length([1,2,3,4,5])


# 4. Values Greater than Second
newList = []

def values_greater_than_second(arr):
    if len(arr) < 2:
        return False
    for x in range(len(arr)):
        if arr[x] > arr[1]:
            newList.append(arr[x])

values_greater_than_second([1,2,6,1,7,9,5])
print(newList)


# 5. This Length, That Value
def length_and_value(size,value):
    newList = []
    for i in range(0, size):
        newList.append(value)
    return newList

print(length_and_value(6,6))