def forward(currentx: int, currenty: int, move: int, aim: int) -> int:
    newx = currentx + move
    newy = currenty + (move * aim)
    return newx, newy


def down(aim: int, move: int) -> int:
    newaim = aim + move
    return newaim


def up(aim: int, move: int) -> int:
    newaim = aim - move
    return newaim


def finalposition(currentx: int, currenty: int) -> int:
    return currentx * currenty


aim = 0
currentx = 0
currenty = 0

with open("./real.data", "r") as datafile:
    while line := datafile.readline().rstrip().split():
        print(f"Direction: {line[0]} Distance: {int(line[1])}")
        if line[0] == "forward":
            currentx, currenty = forward(currentx, currenty, int(line[1]), aim)
        elif line[0] == "down":
            aim = down(aim, int(line[1]))
        elif line[0] == "up":
            aim = up(aim, int(line[1]))
        else:
            continue

    print(
        f"Currentx: {currentx} Currenty: {currenty} Final position: {finalposition(currentx, currenty)}"
    )
