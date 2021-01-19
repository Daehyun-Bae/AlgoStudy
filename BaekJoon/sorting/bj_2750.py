n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

for i in range(n-1):
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            tmp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = tmp        

print('-'*20)
for s in arr:
    print(s)