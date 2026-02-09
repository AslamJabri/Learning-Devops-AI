def binary_search1(arr,target):
    size = len(arr) 
    
    start = 0
    end = size-1
    
    while start <= end:
        mid = (start+end)//2
        #print(mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid-1
        elif arr[mid] < target:
            start = mid+1
    return -1


arr = [1,2,3,4,5,6,7,8,9]
target = 8
print(binary_search1(arr,target))

# Find Target Index

arr1 = [1, 3, 5, 7, 9]
target1 = 7

def binary_search2(arr,target):
    start = 0
    end = len(arr) -1
    
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid -1
        elif arr[mid] < target:
            start = mid+1
            
    return -1

print(binary_search2(arr1,target1))