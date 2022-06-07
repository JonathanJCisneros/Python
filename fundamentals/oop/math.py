class Math:
    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def subtrack(num1, num2):
        return num1 - num2

    @staticmethod
    def multiply(num1, num2):
        return num1 * num2
    
    @staticmethod
    def divide(num1, num2):
        return num1 / num2

    @staticmethod
    def power(num, exponential):
        total = num
        for i in range(1, exponential):
            total *= num
        return total

print(Math.add(20,30))
print(Math.power(4,3))