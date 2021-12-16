def forward(currentx: int, move: int) -> int:
    return currentx + move


def down(currenty: int, move: int) -> int:
    return currenty + move


def up(currenty: int, move: int) -> int:
    return currenty - move


def finalposition(currentx: int, currenty: int) -> int:
    return currentx * currenty


currentx = 0
currenty = 0

with open("./real.data", "r") as datafile:
    while line := datafile.readline().rstrip().split():
        print(f"Direction: {line[0]} Distance: {int(line[1])}")
        if line[0] == "forward":
            currentx = forward(currentx, int(line[1]))
            print(f"Currentx: {currentx}")
        elif line[0] == "down":
            currenty = down(currenty, int(line[1]))
            print(f"Currenty: {currenty}")
        elif line[0] == "up":
            currenty = up(currenty, int(line[1]))
            print(f"Currenty: {currenty}")
        else:
            continue

    print(
        f"Currentx: {currentx} Currenty: {currenty} Final position: {finalposition(currentx, currenty)}"
    )
