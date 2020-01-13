
def binsearch(arr, target, start, end):
    mid = end-start
    if arr[mid] == target:
        return print('Target found at index', mid)
    elif arr[mid] < target:
        return search(arr, target, mid+1, end)
    elif arr[mid] > target:
        return search(arr, target, start, mid-1)
    else:
        return print('Target not found')

arr = [2, 3, 4, 10, 27, 40, 99, 212]
target = 212
ans = 7
length = len(arr)

binsearch(arr, target, 0, length-1)

print('Correct answer is ', ans)