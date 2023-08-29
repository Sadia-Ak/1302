# Sadia Akther 
# sakther1@student.gsu.edu
# SCE
file_name = input("Enter file name : ")
lower_bound = input("Enter lower bound : ")
upper_bound = input("Enter upper bound : ")

# Opening a new file
# 'r' represents the file opening mode i.e. read mode
with open(file_name, 'r') as file:
    
    # readlines() method reads all lines of the file into a list 
    a = file.readlines()
    # len() function finds teh length of the list 
    n = len(a)
    
    # This is the exception handler
    try:
        # index() method finds the index of the word in the list
        i = a.index(lower_bound+'\n')
    except :
        i = 0
        
    # while loop starts
    while(i != n ) :
        print(a[i], end ='')
        
        # If the word is equal to upper_bound, then it breaks the loop
        if ( a[i] == upper_bound+'\n'):
            break
        # increment the index
        i = i + 1 