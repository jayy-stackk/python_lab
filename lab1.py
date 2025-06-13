
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1





target = int(input("Enter the number to search: "))


arr_input = input("Enter the list of numbers separated by spaces: ")
arr = list(map(int, arr_input.split()))



result = linear_search(arr, target)


if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in array")
