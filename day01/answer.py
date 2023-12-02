f = open("./puzzle-input.txt", "r")

sum = 0

for x in f:
    temp = []
    for y in x:
        if y.isalpha() or y == "\n":
            pass
        else:
            temp.append(y)
    z = str(temp[0]) + str(temp[-1])
    print(z)
    sum += int(z)

print(f"Sum of all calibratiion values:  {sum}")


