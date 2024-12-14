'''Getting the subarrays of an array'''
def getSubarray(lst):
    sublists_list = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublists_list.append(lst[i:j])
    return sublists_list
