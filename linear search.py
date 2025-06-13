def linear_search(arr, target):
    print("List of numbers:", arr)
    print("Target to find:", target)

    for index in range(len(arr)):
        if arr[index] == target:
            print(f"Target {target} found at index {index}.")
            return index

    print(f"Target {target} not found in the list.")
    return -1
