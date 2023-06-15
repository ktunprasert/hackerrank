import math

def hourglassSum(arr):
    highestSum = -math.inf
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr) - 1):
            highestSum = max(
                arr[i - 1][j - 1]
                + arr[i - 1][j]
                + arr[i - 1][j + 1]
                + arr[i][j]
                + arr[i + 1][j - 1]
                + arr[i + 1][j]
                + arr[i + 1][j + 1],
                highestSum,
            )
    return highestSum


if __name__ == "__main__":
    hourglassSum(
        [
            [ 1, 1, 1, 0, 0, 0, ],
            [ 0, 1, 0, 0, 0, 0, ],
            [ 1, 1, 1, 0, 0, 0, ],
            [ 0, 0, 2, 4, 4, 0, ],
            [ 0, 0, 0, 2, 0, 0, ],
            [ 0, 0, 1, 2, 4, 0, ],
        ]
    )

    hourglassSum(
        [
            [int(i) for i in n.split()]
            for n in """-1 -1 0 -9 -2 -2
-2 -1 -6 -8 -2 -5
-1 -1 -1 -2 -3 -4
-1 -9 -2 -4 -4 -5
-7 -3 -3 -2 -9 -9
-1 -3 -1 -2 -4 -5""".split(
                "\n"
            )
        ]
    )
    pass
