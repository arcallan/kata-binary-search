# Binary search using recursive function

# Definition of binary search function
def binsearch(arr, target, start, end):
    # Determines midpoint of array
    mid = end-start
    # Compares value at midpoint to target value
    if arr[mid] == target: # Target found
        return print('Target found at index', mid)
    elif arr[mid] < target: # Narrow search to second half of array
        return search(arr, target, mid+1, end)
    elif arr[mid] > target: # Narrow search to first half of array
        return search(arr, target, start, mid-1)
    else: # Target value not in array
        return print('Target not found')

arr = [2, 3, 4, 10, 27, 40, 99, 212] # Array to search
target = 212 # Target to find
length = len(arr) # Length of array to be searched

binsearch(arr, target, 0, length-1) # Search function call
