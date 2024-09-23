# 128. Longest Consecutive Sequence

def longestConsecutive(arr):
    if len(arr)==0: 
        return O

    arr.sort()
    lastSmaller = float('-inf')
    cnt = 0
    longest = 1
    for i in range(len(arr)):
        if arr[i]-1 == lastSmaller:
            cnt += 1
            lastSmaller = arr[i]
        else:
            lastSmaller = arr[i]
            cnt = 1
        longest = max(longest, cnt)
    return longest


def moreOptimal(nums):
    numSet = set(nums)
    longest = 0

    for n in numSet:
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest

arr = [100,4,200,1,3,2]
# print ("Longest Consecutive Number is:", longestConsecutive(arr))
print ("Longest Consecutive Number is:", moreOptimal(arr))