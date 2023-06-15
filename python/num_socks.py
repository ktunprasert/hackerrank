import math


def sockMerchant(n, ar):
    sort = sorted(ar)
    pairs = 0
    for i in range(math.floor(n / 2)):
        if sort[i * 2] == sort[(i * 2) + 1]:
            pairs += 1

    return pairs


if __name__ == "__main__":
    print(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]))
    print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
    pass
