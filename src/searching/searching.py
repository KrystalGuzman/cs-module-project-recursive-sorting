# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # base condition not in array
    if start > end:
        return -1
    # find middle value in search space
    # and compare to key value
    mid = (start + end) // 2
    # base condition (key value found)
    if target == arr[mid]:
        return mid
    # if in lower half
    elif target < arr[mid]:
        return binary_search(arr,target,start,mid-1)
    # if in upper half
    elif target > arr[mid]:
        return binary_search(arr,target,mid+1,end)
        

# print(binary_search([1,3,4,6,8],3,1,8))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    start = 0
    end = len(arr)-1
    if arr[start] < arr[end]:
        isAscending = True
    else:
        isAscending = False
    while (start <= end):
      # calculate the middle of the current range
        mid = start + (end - start) // 2

        if (target == arr[mid]):
            return mid
        # ascending order
        if (isAscending): 
            # target can be in the first half
            if (target < arr[mid]):
              end = mid - 1 
            # target can be in the second half  
            else: # key > arr[mid]
              start = mid + 1 
        # descending order      
        else:         
            # target can be in the first half
            if (target > arr[mid]):
              end = mid - 1 
            # target can be in the second half
            else: # key < arr[mid]
              start = mid + 1 
    return -1 # element not found

# print(agnostic_binary_search([1,3,4,6,8],3))