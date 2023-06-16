from math import factorial
from collections import defaultdict


def sherlockAndAnagrams(s: str) -> int:
    found = defaultdict(int)
    count = 0
    for i in range(1, len(s)):
        for j in range(len(s) - i + 1):
            sub = s[j : j + i]
            sub_key = str(sorted(sub))
            found[sub_key] += 1

    for v in found.values():
        if v < 2:
            continue
        count += factorial(v) / (factorial(2) * factorial(v - 2))

    return int(count)


if __name__ == "__main__":
    print(sherlockAndAnagrams("abba"))
    print(sherlockAndAnagrams("abcd"))
    print(sherlockAndAnagrams("kkkk"))
