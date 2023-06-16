from functools import cmp_to_key
class Player:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score
    def __repr__(self) -> str:
        return f"{name} {score}"
    def comparator(a , b) -> int:
        if b.score - a.score != 0:
            return b.score - a.score

        for l, r in zip(a.name, b.name):
            if l == r:
                continue
            return ord(l) - ord(r)
        return len(a.name) - len(b.name)

if __name__ == "__main__":
    n = int(input())
    data = []
    for i in range(n):
        name, score = input().split()
        score = int(score)
        player = Player(name, score)
        data.append(player)
        
    data = sorted(data, key=cmp_to_key(Player.comparator))
    print("==")
    for i in data:
        print(i.name, i.score)
