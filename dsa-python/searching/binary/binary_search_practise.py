binary_search_array = [1, 3, 5, 7, 9]
target = 7

def binary_search_1(arr,target):
    left = 0
    right = len(arr)-1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1 
        else:
            right = mid -1
print(binary_search_1(binary_search_array,target))       


#First  and last Occurence

arr = [1, 2, 2, 2, 3, 4]
target = 2
def first_occurence(arr,target):
    left = 0
    right = len(arr) -1
    result = -1
    
    while left <= right:
        mid = left + (right - left)//2
        
        if arr[mid] == target:
            result = mid
            right = mid -1
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid -1
    return result

def last_occurence(arr,target):
    left = 0
    right = len(arr) -1
    result = -1
    
    while left <= right:
        mid = left + (right - left)//2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] > target:
            right = mid -1
        else:
            left = mid +1
    return result

print(f'first: {first_occurence(arr,target)}')

print(f"last: {last_occurence(arr,target)}")