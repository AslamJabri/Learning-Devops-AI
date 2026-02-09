# Q1. Find the maximum element in an array

find_max_element = [3,7,1,9,4]

def max_element(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
            
    return max_value

print(max_element(find_max_element))

# Q2. Find the minimum element in an array

find_min_element = [8, 2, 5, 1, 6]

def min_element(arr):
    min_value = arr[0]
    for num in arr:
        if num < min_value:
            min_value = num
    return min_value

print(min_element(find_min_element))


# Q3. Find the sum of all elements

sum_arr_elements = [1,2,3,4]

def sum_arr(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

print(sum_arr(sum_arr_elements))

#Q4. Count how many elements are even

count_even_arr = [1, 2, 3, 4, 6]

def count_even_elements(arr):
    count = 0
    
    for num in arr:
        if num % 2 ==0:
            count +=1
            
    return count

print(count_even_elements(count_even_arr))

# Count how many elements are greater than k

count_elements = [2, 7, 4, 9, 1]
k = 5

def count_greater_elements(arr,k):
    count = 0
    for num in arr:
        if num > k:
            count +=1
            
    return count
print(count_greater_elements(count_elements,k))

#Check if the array is sorted (non-decreasing)

unchecked_sorted_arr = [1,2,3]

def check_sorted_arr(arr):
    for i  in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

print(check_sorted_arr(unchecked_sorted_arr))
        
#Find the second largest element

element_arr = [10, 5, 20, 8, 15]

def second_largest_arr(arr):
    largest = float('-inf')
    second_largest = float('-inf')
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num < largest and num > second_largest:
            second_largest = num
    return second_largest

print(second_largest_arr(element_arr))    

#🟡 Q8. Find the frequency of each element

frequency_arr = [1, 2, 2, 3, 1]

def count_frequency(arr):
    frequency = {}
    
    for num in arr:
        if num in frequency:
            frequency[num] +=1
            
        else:
            frequency[num] =1
            
    return frequency

print(count_frequency(frequency_arr))


# 🟡 Q9. Move all negative numbers to the end (order doesn’t matter)

negative_arr = arr = [1, -2, 3, -4, 5]

def move_negative(arr):
    positive = []
    negative = []

    for num in arr:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)

    return positive + negative

print(move_negative(negative_arr))


# 10. Find the missing number from 0..n

missing_number_arr = [3,0,1,2,5]

def find_missing_number(arr):
    actual_sum =0
    n = len(arr)
    expected_sum =  n * (n+1) //2
    for num in arr:
        actual_sum += num
    
    missing_num = expected_sum - actual_sum
    return missing_num
print(find_missing_number(missing_number_arr))