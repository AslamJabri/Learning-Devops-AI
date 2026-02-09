binary_arr = [1, 3, 5, 7, 9]
target = 7

def binary_search(arr,target):
    right = len(arr)-1
    left =0
    
    while left <= right:
        mid = left + (right - left)//2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1
print(binary_search(binary_arr,target))