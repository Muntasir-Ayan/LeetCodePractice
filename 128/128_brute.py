# 128. Longest Consecutive Sequence

def linerSearch(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return True
        
    return False

def longestConsecutive(num):
    longest = 1
    for i in range(len(arr)):
        num = arr[i]
        cnt = 1
        while linerSearch(arr, num+1):
            num +=1
            cnt +=1
        longest = max(longest, cnt)
    return longest

arr = [0,3,7,2,5,8,4,6,0,1]
print ("Longest Consecutive Number is:", longestConsecutive(arr))

# time complexity O(n^2)
