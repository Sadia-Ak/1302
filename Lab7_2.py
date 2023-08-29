# Sadia Akther 
# sakther1@student.gsu.edu
# SCE
file_name = input()
bound1 = input()
bound2 = input()

with open(file_name) as file_handle:
    list1 = [line.strip() for line in file_handle]

out = [x for x in list1 if x >= bound1 and x <= bound2]

out.sort()
print("The words are:")
print('\n'.join(map(str, out))) 
