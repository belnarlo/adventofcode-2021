count = 0
increases = 0
linelist = []

with open("./real.data", "r") as datafile:
    for line in datafile:
        linelist.append(int(line.rstrip()))

print(len(linelist))
while count < (len(linelist) - 2):
    if count == 0:
        prevvalue = sum(linelist[count : count + 3])
        print(f"Firstvalue {prevvalue} increases {increases}")
    else:
        value = sum(linelist[count : count + 3])
        if value > prevvalue:
            increases += 1
            print(f"Value: {value} Prevvalue {prevvalue} Increases {increases}")
            prevvalue = value
        else:
            print(f"Value: {value} Prevvalue {prevvalue} Count {count}")
            prevvalue = value
            prevvalue = value
    count += 1

print(increases)
