# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # set indices
    a = 0
    b = 0
    # loop through all
    for i in range(elements):
        # if a is out of range
        if a >= len(arrA):
            # add to merged_arr
            merged_arr[i] = arrB[b]
            # increase index
            b += 1
        # if b is out of range
        elif b >= len(arrB):
            # add to merged_arr
            merged_arr[i] = arrA[a]
            # increase index
            a += 1
        # if a is smaller
        elif arrA[a] < arrB[b]:
            # add to merged_arr
            merged_arr[i] = arrA[a]
            # increase index
            a += 1
        # if b is smaller
        else:
            # add to merged_arr
            merged_arr[i] = arrB[b]
            # increase index
            b += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # base case: when list gets down to length 1
    if len(arr) > 1:
        # divide array into left and right halves
        left = merge_sort(arr[:len(arr)//2])
        right = merge_sort(arr[len(arr)//2:])
        #merges two arrays
        arr = merge(left,right)
        
    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input

def merge_in_place(arr, start, mid, end):
	# start2 = first element in the right half of the list
    start2 = mid + 1

    # If sorted, do nothing
    if arr[mid] <= arr[start2]:
        return

    # Two pointers to maintain start
    # of both arrays to merge
    while start <= mid and start2 <= end:

        # If element 1 is in right place
        if arr[start] <= arr[start2]:
            start += 1

        else:
            # value holders
            value = arr[start2]
            index = start2

            # Shift all the elements between element 1
            # and element 2, right by 1.
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1
			
	# we don't return anything in in-place functions
	# since we're directly mutating the input array

def merge_sort_in_place(arr, l, r):
    if r - l > 0:
        mid = int((l+r)//2)
        # sort first and second halves
        merge_sort_in_place(arr,l,mid)
        merge_sort_in_place(arr,mid+1,r)
        merge_in_place(arr,l,mid,r)
    return arr

print(merge_sort_in_place([4,3,5,6,2,8,7],0,6))
print(merge_sort_in_place([1],0,0))