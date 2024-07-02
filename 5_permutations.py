n = int(input())
arr = [i for i in range(1, n+1)]
odds = [i for i in arr if i % 2 != 0]
evens = [i for i in arr if i % 2 == 0]
answer = evens+odds

if n == 2 or n == 3:
    print("NO SOLUTION")

else:
    for i in range(len(answer)):
        print(answer[i], end = " ")