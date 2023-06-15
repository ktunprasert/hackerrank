def checkMagazine(magazine, note):
    available = {}
    for word in magazine:
        if word in available:
            available[word]+=1
        else:
            available[word]=1

    for word in note:
        if word not in available or available[word] <= 0:
            print("No")
            return

        available[word] -= 1

    print("Yes")

if __name__ == "__main__":
    checkMagazine(
        "two times three is not four".split(), "two times two is four".split()
    )
    checkMagazine(
        "ive got a lovely bunch of coconuts".split(), "ive got some coconuts".split()
    )
    checkMagazine("give me one grand today".split(), "give one grand today".split())
