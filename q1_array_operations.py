# Q1. Array operations: search, sort, list, traverse, insert

arr = [45, 12, 78, 33, 9, 56]


def search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def list_all(arr):
    print("Array:", arr)


def traverse(arr):
    for i in range(len(arr)):
        print("Index", i, ":", arr[i])


def insert(arr, pos, value):
    if pos < 0 or pos > len(arr):
        print("Invalid position")
        return
    arr.append(0)
    for i in range(len(arr) - 1, pos, -1):
        arr[i] = arr[i - 1]
    arr[pos] = value


# A. Search
key = 33
index = search(arr, key)
if index != -1:
    print(key, "found at index", index)
else:
    print(key, "not found")

# B. Sort
sort(arr)
print("After sorting:", arr)

# C. List
list_all(arr)

# D. Traverse
traverse(arr)

# E. Insert
insert(arr, 2, 20)
print("After inserting 20 at index 2:", arr)
