from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in arr:
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1
    return count

if __name__ == "__main__":
    print(countTriplets([2, 4, 6], 2))  # 0
    print(countTriplets([1, 2, 2, 4], 2)) # 2
    print(countTriplets([1, 3, 9, 9, 27, 81], 3)) # 6
    print(countTriplets([1, 5, 5, 25, 125], 5))  # 4
