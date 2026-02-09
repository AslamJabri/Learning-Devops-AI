unsorted_list = [12,25,11,34,90,22]

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr
print(selection_sort(unsorted_list))


#🟢 Problem 3: Minimum Swaps to Sort (Medium)
arr = [4,3,2,1]
def selection_sort2(arr):
    n = len(arr)
    count = 0
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j      
        if min_index != i:       
            arr[i],arr[min_index] = arr[min_index],arr[i]
            count+=1 
        
    return count

print(selection_sort2(arr))
            
    