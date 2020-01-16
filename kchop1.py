# Binary search using recursive function

# Definition of binary search function
def binsearch(arr, target, start, end):
    # Determines midpoint of array
    mid = round((end+start)/2)
    # Compares value at midpoint to target value
    if arr[mid] == target: # Target found
        return print('Target found at index', mid)
    elif end-start < 1: # Down to the last item to search and still haven't found it
        return print('Target not found')
    elif arr[mid] < target: # Narrow search to second half of array
        return binsearch(arr, target, mid+1, end)
    elif arr[mid] > target: # Narrow search to first half of array
        return binsearch(arr, target, start, mid-1)
        

arr = [2, 3, 4, 10, 11, 27, 40, 99, 212] # Array to search
target = 11 # Target to find
length = len(arr) # Length of array to be searched

binsearch(arr, target, 0, length-1) # Search function call
