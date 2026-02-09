#🟢 Q1. Reverse an array in-place

arr = [1,2,3,4,5]

def reverse_array(arr):
    left = 0
    right = len(arr)-1
    
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left +=1
        right -=1
    return arr

print(reverse_array(arr))


#🟢 Q2. Check if a string is a palindrome

s ="madau"

def palindrome(s):
    left = 0
    right = len(s) -1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left +=1
        right -=1
    return True
print(palindrome(s))

# 🟢 Q3. Remove duplicates from a sorted array (IN-PLACE)

duplicate_elements = [1, 1, 2, 2, 3]

def remove_duplicate_elements(arr):
    
    if not arr:
        return arr
    j = 0
    for i in range(1,len(arr)):
        if arr[i] != arr[j]:
            j+=1
            arr[j] = arr[i]

        
    return arr[:j+1]
print(remove_duplicate_elements(duplicate_elements))

#🔜 Next: Q4 — Move all zeros to the end (IN-PLACE)

arr_zeroes = [0, 1, 0, 3, 12]

def move_zeros(arr):
    slow= 0
    for fast in range(len(arr)):
        if arr[fast] != 0:
           arr[slow] = arr[fast]
           slow +=1
    for i in range(slow,len(arr)):
        arr[i] = 0
           
    return arr
print(move_zeros(arr_zeroes))

#🟢 PART 1: FIXED-SIZE SLIDING WINDOW

arr_sliding_arr = [2, 1, 5, 1, 3, 2]
k = 3

def max_sum_subarray(arr, k):
    left = 0
    max_sum = 0
    window_sum = 0
    
    for right in range(len(arr)):
        window_sum += arr[right]
        
        if right >= k -1:
            if window_sum > max_sum:
                max_sum = window_sum
            window_sum -= arr[left]
            left +=1
    return max_sum
print(max_sum_subarray(arr_sliding_arr,k))

#🟢 Q2. Average of all subarrays of size k
average_sliding_arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5


def average_subarrays(arr, k):
    left = 0 
    max_sum = []
    window_sum =0
    
    for right in range(len(arr)):
        window_sum += arr[right]
        
        if right >= k - 1 :
            max_sum.append(window_sum/k)
            window_sum -= arr[left]
            left +=1
            
    return max_sum
            
            
print(average_subarrays(average_sliding_arr,k))

#VARIABLE-SIZE SLIDING WINDOW
#🟢 Q3. Smallest subarray with sum ≥ S

sub_arr = [2, 1, 5, 2, 3, 2]
S = 7

def smallest_sub_arr(arr,k):
    left = 0
    min_len = float('inf')
    window_sum = 0
    
    for right in range(len(arr)):
        window_sum += arr[right]
        
        while window_sum >= S:
             current_len = right - left +1
             
             if current_len < min_len:
                 min_len = current_len
                 
             window_sum -= arr[left]
             left +=1
             
    if min_len == float('inf'):
        return 0
    return min_len
                
print(smallest_sub_arr(sub_arr,S))