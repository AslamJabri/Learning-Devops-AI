arr = [3,2,5,1,7,6]

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
                
        if not swapped:
            break
                
    return arr

print(bubble_sort(arr))




arr2 = [20,3,4,2,5,1,8,10]

def bubble_sort2(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            swapped = True
        if not swapped:
            break 
                
    return arr


print(bubble_sort2(arr2))


#Problem 1: Early Exit Detection (Easy → Medium)

arr3 = [1, 2, 3, 4, 5]

def bubble_sort3(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr
print(bubble_sort3(arr3))

#Problem 2: Bubble Sort Swap Count (Medium)

arr4=[3,2,1]

def bubble_sort4(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
                count +=1
        if not swapped:
            break
    return count
print(bubble_sort4(arr4))