n = int(input())
arr = list(int(n) for n in input().split()[:n])
moves = 0
diff = 0

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        diff = arr[i] - arr[i+1]
        arr[i+1] += diff
        moves += diff

print(moves)    