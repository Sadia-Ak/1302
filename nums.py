def one(number):
    return number ** 2

def two(number):
    return number * 3

def three(number):
    return one(number) - two(number)

def one1(number):
    return number - 8

def two1(number):
    return number + 2

def three1(number):
    return one(number) * two(number)

def four1(number):
    return three(number)

def one2(number):
    return number + 6

def two2(number):
    return number - 4

def three2(number):
    return number * 1 


print(three2(5))
print(three1(5))
print(four1(5))