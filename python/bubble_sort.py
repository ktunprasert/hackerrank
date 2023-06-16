def countSwaps(a: list) -> None:
    swaps = 0
    for _ in range(len(a) - 1):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1

    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a)-1]}")

if __name__ == "__main__":
    countSwaps([6,4,1])
