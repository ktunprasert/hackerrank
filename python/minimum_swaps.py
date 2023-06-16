def minimumSwaps(arr: list[int]) -> int:
    swaps = 0
    i = 0
    while i < len(arr):
        if arr[i] != i + 1:
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
            swaps += 1
        else:
            i += 1
    return swaps


if __name__ == "__main__":
    print(minimumSwaps([1, 3, 2, 5, 4]))  # 2
    print(minimumSwaps([4, 3, 1, 2]))  # 3
    print(minimumSwaps([2, 3, 4, 1, 5]))  # 3
    print(minimumSwaps([1, 3, 5, 2, 4, 6, 7]))  # 3
