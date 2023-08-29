# Sadia Akther 
# sakther1@student.gsu.edu
# SCE

num1 = int(input("The lowest bound:"))
# the lowest bound is 1
num2 = int(input("The higestest bound:"))
# the highest bound is 100
for i in range(num1,num2+1):
	if i % 5 == 0: 
		print(i, "is divisible by 5") 