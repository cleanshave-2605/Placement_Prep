'''Getting the subarrays of an array'''
def getSubarray(arr):
    n = len(arr)
    result = [[]]
    for i in range(n):
        result += [sub + [arr[i]] for sub in result]
    return result

print(getSubarray([1, 2, 3, 4]))