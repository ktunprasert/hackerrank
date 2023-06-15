def jumpingOnClouds(c):
    start = 0
    jumps = 0
    while start < len(c) - 1:
        if start + 2 < len(c) and c[start + 2] == 0:
            start += 2
        else:
            start += 1

        jumps += 1

    return jumps


if __name__ == "__main__":
    print(jumpingOnClouds([0, 1, 0, 0, 0, 1, 0]))  # 4
    print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))  # 3
    print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))  # 4

    pass
