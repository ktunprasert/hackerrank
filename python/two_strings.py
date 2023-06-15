def twoStrings(s1, s2):
    checked = {}
    substr_len = 1
    while substr_len < len(s1):
        for j in range(len(s1) - substr_len + 1):
            sub = s1[j : j + substr_len]
            if sub in checked:
                continue

            checked[sub] = True

            for k in range(len(s2) - substr_len + 1):
                check_sub = s2[k : k + substr_len]
                if sub == check_sub:
                    return "YES"

        substr_len += 1
    return "NO"


if __name__ == "__main__":
    print(twoStrings("hello", "world"))
    print(twoStrings("aa", "ba"))
    print(twoStrings("x", "y"))
