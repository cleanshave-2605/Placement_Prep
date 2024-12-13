'''Suppose you are given a list of numbers in a random order. However, you need to get the indices of the elements if they were sorted.
The easier way to do so is present in the code below'''
def getIndices(arr):
    ord = list(range(len(arr)))
    ord.sort(key=lambda x : (arr[x], x))
    return ord