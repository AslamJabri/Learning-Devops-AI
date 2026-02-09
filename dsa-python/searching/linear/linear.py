my_list = [4,2,3,89,10,23]
target = 89
def linear_search(arr,target):
    size = len(arr)
    for index in range(0,size):
        if arr[index] == target:
            return index
        
    return -1            
print(linear_search(my_list,target))

# Find Index of Target
arr = [5, 3, 7, 1]
target = 7

def linear(arr,target):
    size = len(arr)
    for index in range(0,size):
        if arr[index] == target:
            return index
        
    return -1

print(linear(arr,target))

# Check if Element Exists
checking_arr = [10, 20, 30]
check = 20

def check_element(arr,target):
    size = len(checking_arr)
    for i in range(0,size):
        if arr[i] == target:
            return True
    return False

print(check_element(checking_arr,check))

# Count Occurrences

counting_arr = [1, 2, 1, 3, 1]
count_target = 1

def count(arr,target):
    count = 0
    
    for i in range(0,len(arr)):
        if arr[i] == target:
            count += 1
            
    return count

print(count(counting_arr,count_target))