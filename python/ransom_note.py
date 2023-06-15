def checkMagazine(magazine, note):
    m_s = set(magazine)
    n_s = set(note)

    if len(n_s & m_s) == len(note):
        print("Yes")
        return

    print("No")


if __name__ == "__main__":
    checkMagazine(
        "two times three is not four".split(), "two times two is four".split()
    )
    checkMagazine(
        "ive got a lovely bunch of coconuts".split(), "ive got some coconuts".split()
    )
    checkMagazine("give me one grand today".split(), "give one grand today".split())
