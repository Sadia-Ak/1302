# Sadia Akther 
# sakther1@student.gsu.edu
# SCE

# problem 1
import math
x = float(input())
y = float(input())
z = float(input())
your_value1 = pow(x,z)
your_value2=x**(y**z)
your_value3=math.sqrt(x**z)
your_value3=math.sqrt(x**z)
your_value4 = x-y
print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(your_value1,your_value2,your_value3,your_value4))

# problem 2

user_num = int(input())
div_num = int(input())
print(user_num//div_num , (user_num//div_num)//div_num , ((user_num//div_num)//div_num)//div_num )


# problem 3
list1 = [10, 20, 5, 45, 95, 105]
#a
print(min(list1))
#b
print(max(list1))
#c
print(sum(list1))
#c
list1.remove(105)
print(list1)

