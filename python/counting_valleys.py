def countingValleys(steps, path):
    sea_level = 0
    valleys = 0
    in_valley = False

    for step in path:
        if step == "D":
            sea_level -= 1
        else:
            sea_level += 1

        if sea_level < 0 and in_valley == False:
            valleys += 1

        in_valley = sea_level < 0

    return valleys


if __name__ == "__main__":
    print(countingValleys(8, "DDUUUUDD"))
