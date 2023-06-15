import math


def sockMerchant(n, ar):
    socks = {}
    pairs = 0

    for sock_num in ar:
        if sock_num in socks:
            socks[sock_num] += 1
        else:
            socks[sock_num] = 1

    for count in socks.values():
        pairs += math.floor(count / 2)

    return pairs


if __name__ == "__main__":
    print(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]))
    print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
    pass
