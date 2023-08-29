# Sadia Akther 
# sakther1@student.gsu.edu
# SCE

def merge_sort(Arr):
    if len(Arr) > 1:
        mid = len(Arr) // 2
        left = Arr[:mid]
        right = Arr[mid:]
        merge_sort(left)
        merge_sort(right)
       
        i = 0
        j = 0
        k = 0
       
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                Arr[k] = left[i]
                i = i + 1
            else:
                Arr[k] = right[j]
                j = j + 1
            k = k + 1
            while i < len(left):
                Arr[k] = left[i]
                i = i + 1
                k = k + 1
            while j < len(right):
                Arr[k] = right[j]
                j = j + 1
                k = k + 1

Arr = [5, 2, 8, 3, 1, 6, 9, 7]
merge_sort(Arr)
print(Arr)