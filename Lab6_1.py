# Sadia Akther 
# sakther1@student.gsu.edu
# SCE
def all_permutations(nameList, permList):
    if(len(nameList) == 0):
        value = ', '.join(permList)+" " 
        print(value)  
    else:
        for i in range(len(nameList)):
            all_permutations(nameList[:i] + nameList[i+1:], permList + nameList[i:i+1])
if __name__ == "__main__":
    nameList=input().split(' ')
    permList = []
    all_permutations(nameList,permList)

