from math import factorial


def sherlockAndAnagrams(s: str) -> int:
    i = 1
    found = {}
    count = 0
    while i <= len(s) - 1:
        for j in range(0, len(s)):
            sub = s[j : j + i]
            sub_key = sorted(sub).__str__()

            if len(sub) < i:
                continue

            if sub_key in found:
                found[sub_key] += 1
            else:
                found[sub_key] = 1
        i += 1

    for v in found.values():
        if v < 2:
            continue
        count += int(factorial(v)) / (factorial(2) * factorial(v - 2))

    return int(count)


if __name__ == "__main__":
    print(sherlockAndAnagrams("abba"))
    print(sherlockAndAnagrams("abcd"))
    print(sherlockAndAnagrams("kkkk"))
