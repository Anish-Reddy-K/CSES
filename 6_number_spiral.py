t = int(input())

results = []

for i in range(t):
    y, x = map(int, input().split())

    d = max(x,y) 
    diag = (d*d) - (d-1)
    answer = 0

    if d%2==0:
        if y==x:
            answer = diag
        elif y>x:
            answer = diag + (y-x)
        elif y<x:
            answer = diag - (x-y)
    else:
        if y==x:
            answer = diag
        elif y>x:
            answer = diag - (y-x)
        elif y<x:
            answer = diag + (x-y)

    results.append(answer)

for result in results:
    print(result)