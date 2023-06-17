from collections import Counter

def makeAnagram(a: str, b: str) -> int:
    c1 = Counter(a)
    c2 = Counter(b)

    return sum((c1-c2).values()) + sum((c2-c1).values())

if __name__ == "__main__":
    print(makeAnagram("cde", "abc"))  # 4
    print(makeAnagram("cde", "dcf"))  # 2
    print(makeAnagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke"))  # 30
