count = 0
increases = 0

with open("./real_1.data", "r") as datafile:
    while line := datafile.readline().rstrip():
        if count != 0 and int(line) > lineprev:
            increases += 1
        count += 1
        lineprev = int(line)

print(increases)
