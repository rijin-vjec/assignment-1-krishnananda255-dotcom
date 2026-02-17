arr = list(map(int, input().split()))
key = int(input())

index = -1
for i in range(len(arr)):
    if arr[i] == key:
        index = i
        break

print(index)
