




def maxint(arr, nums):
    arr = sorted(arr)
    #x = len(arr) - nums
    arr = arr[len(arr)-nums:len(arr)]
    answer = 1
    for a in arr:
        answer *= a
    return answer


print(maxint([10,3,-27,-1], 3))
print(maxint([14,29,-28,39,-16,-48], 4))