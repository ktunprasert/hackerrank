def rotLeft(a: list[int], d: int):
    while d > 0:
        fst = a.pop(0)
        a = [*a, fst]
        d -= 1
    return a


if __name__ == "__main__":
    print(rotLeft([1, 2, 3, 4, 5], 2))
