def alternatingCharacters(s: str) -> int:
    count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count+=1
    return count

if __name__ == "__main__":
    assert alternatingCharacters("AABAAB") == 2
    assert alternatingCharacters("AAAA") == 3
    assert alternatingCharacters("BBBBB") == 4
    assert alternatingCharacters("ABABABAB") == 0
    assert alternatingCharacters("BABABA") == 0
    assert alternatingCharacters("AAABBB") == 4
