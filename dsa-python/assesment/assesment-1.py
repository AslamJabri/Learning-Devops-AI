#Find the largest and second largest element in an array
arr = [10, 5, 20, 8, 15]

def finding_element(arr):
    first_element = float('-inf')
    second_element = float('-inf')
    
    for num in (arr):
        if num > first_element:
            second_element = first_element
            first_element = num
        elif num < first_element and num > second_element:
            second_element = num
  

    
    return f'first element = {first_element}, second element = {second_element}'



            
    #return largest

print(finding_element(arr))




#Check if an array is sorted (non-decreasing)

check_sorted_arr = [1,2, 2, 4, 7]

def check_sorted(arr):
    for i in range(len(arr)-1):
        first = arr[i]
        second = arr[i+1]
        if first > second:
            return False
    return True

print(check_sorted(check_sorted_arr))    

#Count elements greater than k
count_arr = [3, 7, 1, 9, 4, 6]
k = 5
def counting_element(arr,k):
    count = 0
    for num in arr:
        if num > k:
            count +=1
    return count

print(counting_element(count_arr,k))

#Rotate array by k steps (extra space allowed first)


unroated_arr = [1, 2, 3, 4, 5]
steps_k = 2

def rotate_array(arr,k):
    n = len(arr)
    k = k % n
    print(k)
    new_arr = []
    
    for i in range(n-k,n):
        new_arr.append(arr[i])
    for j in range(0,n-k):
        new_arr.append(arr[j])
        
    return new_arr

print(rotate_array(unroated_arr,steps_k))
         