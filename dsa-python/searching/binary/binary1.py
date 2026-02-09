arr = [2, 5, 8, 12, 16, 23, 38]
target = 16

def binary_search(arr,target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = left + (right-left)//2
        
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right  = mid-1
        else:
            left =mid +1
            
print(binary_search(arr,target))


    
arr2 = [1, 3, 5, 7, 9, 11]
target2 = 7

def binary_search2(arr,target):
    left = 0
    right = len(arr)-1
    
    while left <= right:
        mid = left + (right-left)//2
        
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid -1
            
        else:
            left = mid +1
    return -1

print(binary_search2(arr2,target2))

arr3 = [1,2,2,2,3,4,5]
target3 = 2
def first_occurence(arr,target):
    left,right = 0,len(arr)-1
    result = -1
    while left <= right:
        mid = left + (right-left)//2
        if arr[mid] == target:
            result = mid
            right = mid -1
        elif target < arr[mid]:
            right = mid -1
        else:
            left = mid +1
            
    return result
print(first_occurence(arr3,target3))


def last_occurence(arr,target):
    left,right,result = 0,len(arr)-1,-1
    
    while left <= right:
        mid = left + (right-left)//2
        if arr[mid] == target:
            result = mid
            left = mid +1
        elif target < arr[mid]:
            right = mid-1
        else:
            left = mid +1
    return result

print(last_occurence(arr3,target3))


arr4 = [1,2, 2, 2, 2, 2,5]
target4 = 2

        
def first_occurence_dry(arr,target):
        left,right,result,count = 0,len(arr)-1,-1,0
        
        while left <= right:
            mid = left + (right-left)//2
            
            if arr[mid] == target:
                result = mid
                count += 1
                right = mid -1
                
            elif target < arr[mid]:
                right = mid -1
            else:
                left = mid + 1
                
        return mid,result,count
        
def last_occurence_dry(arr,target):
    left,right,result,count = 0,len(arr)-1,-1,0
    while left <= right:
        mid = left + (right-left)//2
        
        if arr[mid] == target:
            result = mid
            count +=1
            left = mid + 1
            
        elif target < arr[mid]:
            right = mid -1
            
        else:
            left = mid + 1
            
    return mid,result,count

print(first_occurence_dry(arr4,target4))
print(last_occurence_dry(arr4,target4))