def minimumBribes(q):
    bribes = 0

    for i, n in enumerate(q):
        if (n-1) - i > 2:
            print("Too chaotic")
            return
        for j in range(max(0, n-2), i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)

if __name__ == "__main__":

    minimumBribes([1, 2, 3])
    minimumBribes([2, 1, 3])
    minimumBribes([2, 1, 5, 3, 4])
    minimumBribes([2, 5, 1, 3, 4])
    minimumBribes([1, 4, 2, 3, 5])
    minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
    pass
