
# 1
arr1 = [4, 1, 2, 1, 2]
unique = [int(item) for item in set(arr1) if arr1.count(item) == 1]
print(unique[0])

# 2
arr2 = [4, 1, 2, 1, 2]
for item in arr2:
    if arr2.count(item) == 1:
        print(item)

