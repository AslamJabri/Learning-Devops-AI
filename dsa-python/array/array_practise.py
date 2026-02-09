#Find the second largest element in an array.

arr = [10,5,20,8]

def second_largest_element(arr):
    largest = float('-inf')
    second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num < largest and num > second:
            second = num
            
    return second

print(second_largest_element(arr))

#Count how many elements are greater than a given value k.

count_elements = [3, 7, 1, 9, 4]
k = 4

def greater_elements(arr,k):
    count = 0
    for num in arr:
        if num > k:
            count+=1
        
    return count
print(greater_elements(count_elements,k))


# Check if an array is sorted in non-decreasing order.

checking_sorted_array = [1, 2, 2, 5, 7]

def sorted_arr(arr):
    for num in range (len(arr)-1):
        if arr[num] > arr[num+1]:
            return False
        
    return True

print(sorted_arr(checking_sorted_array))

#Reverse the array in-place.

reversing_arr=[1,2,3,4]

def rev_arr(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left +=1
        right -=1
    return arr

print(rev_arr(reversing_arr))


#Palindrome Check

string = "hello"

def is_palindrome(s):
    left = 0
    right = len(s) -1
    while left < right:
        if s[left] != s[right]:
            return False
        left+=1
        right -=1
    return True
        
print(is_palindrome(string))

#Problem 2 — Pair Sum in Sorted Array (Easy)

sum_arr = [1,2,4,6,10]
target = 8

def pain_sum(arr,target):
    left = 0
    right = len(arr)-1
    
    while left < right:
        number = arr[left] + arr[right]
        if number > target:
            right -=1
        elif number < target:
            left +=1
        elif number == target:
             return True,arr[left],arr[right]
    return False
            
print(pain_sum(sum_arr,target))


duplicated_arr = [1,1,2,2,3]

def remove_duplicates(arr):
    left = 0
    for i in range(1,len(arr)):
        if arr[i] != arr[left]:
            left+=1
            arr[left] = arr[i]

    return arr[:left+1]
    
    

print(remove_duplicates(duplicated_arr))




# sliding window

sliding_window_arr = [1,2,3,1,2,4,6]
k = 3

def sliding_window(arr,k):
    max_sum = 0
    left = 0
    window_sum = 0
    for right in range(len(arr)):
        window_sum += arr[right]
        if right >= k-1:
            if window_sum > max_sum:
                max_sum=window_sum
            window_sum -= arr[left]
            left +=1
    return max_sum
    
print(sliding_window(sliding_window_arr,k))

# Problem: Average of Subarrays of Size K

arr_sliding = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5


def sliding_practise(arr,k):
    result = []
    window_sum = 0
    left = 0
    for right in range(len(arr)):
        window_sum += arr[right]
        
        if right >= k-1:
            result.append(window_sum/k)
            window_sum -= arr[left]
            
            left += 1
    return result

print(sliding_practise(arr_sliding,k))
        
    
# Problem: Maximum Sum Subarray of Size K

s_arr = [2, 3, 4, 1, 5]
s_k = 2
def max_sum(arr,k):
    max_sum = 0
    left = 0
    window_sum = 0
    
    for right in range(len(arr)):
        window_sum += arr[right]
        
        if right >= k-1:
            if window_sum > max_sum:
                max_sum = window_sum
            window_sum -= arr[left]
            left +=1
    return max_sum

print(max_sum(s_arr,s_k))


def sliding_window_variable(arr,target):
    left = 0
    min_length = float('inf')
    current_sum = 0
    for right in range(len(arr)):
        current_sum += arr[right]
        
        while current_sum >= target:
            current_window_size = right - left + 1
            
            if current_window_size < min_length:
                min_length = current_window_size
            
            current_sum -= arr[left]
            left +=1
        
    return min_length if min_length != float('inf') else 0
    
    
    
s_arr = [2, 1, 5, 2, 3, 2]
s_target = 7
print(sliding_window_variable(s_arr,s_target))


# Practice Problem — Variable Sliding Window

# Longest subarray with sum ≤ S

l_arr = [1, 2, 1, 0, 1, 1, 0]
l_target = 4

def longest_subarray(arr,target):
    left = 0
    current_sum = 0
    result = 0
    for right in range(len(arr)):
        current_sum += arr[right]
        
        while current_sum > target:
            current_sum -= arr[left]
            left +=1
            
        current_window_length = right-left +1
        
        result = max(result,current_window_length)
    return result
    
    
    
    
print(longest_subarray(l_arr,l_target))
    
    

# 🧩 Problem: Longest Substring Without Repeating Characters

s = "abcabcbb"

def substring(s):
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left +=1
            
        char_set.add(s[right])
        
        max_len = max(max_len,right-left +1)
    return max_len
    
    
    
    
    
    
print(f"substring : {substring(s)}")