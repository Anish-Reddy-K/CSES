n = int(input())
arr = [0] * (n+1)

nums = list(int(n) for n in input().strip().split()[:n-1])

for num in nums:
    arr[num] = num

for i in range(1, n+1):
    if arr[i] == 0:
        print(i)  

# Alternate Approach 

# n = int(input())
# total_sum = n * (n+1)//2

# nums = list(int(n) for n in input().strip().split()[:n-1])

# nums_sum = 0
# for i in nums:
#     nums_sum += i

# print(total_sum - nums_sum)