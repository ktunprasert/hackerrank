def rotLeft(a: list[int], d: int):
    return [*a[d:], *a[:d]]


if __name__ == "__main__":
    print(rotLeft([1, 2, 3, 4, 5], 2))
