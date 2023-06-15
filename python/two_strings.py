def twoStrings(s1, s2):
    return "YES" if len(set(s1) & set(s2)) else "NO"


if __name__ == "__main__":
    print(twoStrings("hello", "world"))
    print(twoStrings("aa", "ba"))
    print(twoStrings("x", "y"))
