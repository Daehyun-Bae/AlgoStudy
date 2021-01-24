MAX = 3
arr1 = [[[0]*MAX for _ in range(MAX)] for __ in range(MAX)]
arr2 = [[[0] * MAX] * MAX] * MAX

arr1[0][0][0] = arr1[0][1][0] + arr1[0][0][1] + arr1[1][0][0]
arr2[0][0][0] = arr2[0][1][0] + arr2[0][0][1] + arr2[1][0][0]

for arr_r in arr1:
    print(arr_r)
print('-'*80)
for arr_r in arr2:
    print(arr_r)

print('-'*30, 'Add 1 arr[0][1][0]', '-'*30)


arr1[0][1][0] = 1
arr2[0][1][0] = 1

for arr_r in arr1:
    print(arr_r)
print('-'*80)
for arr_r in arr2:
    print(arr_r)
