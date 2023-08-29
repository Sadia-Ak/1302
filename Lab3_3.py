# Sadia Akther 
# sakther1@student.gsu.edu
# SCE
def in_order(x):
    if len(x) < 2:
        return True
 
    for i in range(1, len(x)): 
        if (x[i]<x[i-1]):
            return False
    return True

if __name__ == '__main__':
    # Testing out of order 
    num  = [5, 6, 7, 8, 3]
    if in_order(num):
        print('In order')
    else:
        print('Not in order')

    # Testing in order 
    num = [5, 6, 7, 8, 10]
    if in_order(num):
        print('In order')
    else:
        print('Not in order')