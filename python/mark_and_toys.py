def maximumToys(prices: list[int], k: int) -> int:
    asc_prices = sorted(prices)
    max_toys = 0

    for price in asc_prices:
        if k - price < 0:
            break
        k -= price
        max_toys += 1

    return max_toys

if __name__ == "__main__":
    print(maximumToys([1,2,3,4], 7)) # 3
    print(maximumToys([1, 12, 5 ,111, 200, 1000, 10], 50)) # 4
