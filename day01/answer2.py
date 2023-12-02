f = open("./puzzle.txt", "r")
iter = 1
sum = 0

# dictionary of numbers in words
numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

for x in f:
    
    # temp = {key(value+position): value, position}
    temp = {}
    
    # checks if there are digits and adds to dict
    for a, y in enumerate(x):
        if y.isalpha() or y == "\n":
            pass
        else:
            k = y + str(a)
            temp[k] = [int(y)]
            temp[k] += [a]
            
    #checks if there are sub string numbers and adds to dict
    for u in numbers:
        if x.find(u) != -1:
            val = numbers[u]
            pos = x.find(u)
            k =  str(val) + str(pos)
            temp[k] = [val]
            temp[k] += [pos]
    
    # sorts the dict by their positions
    sortedtemp = sorted(temp.items(), key=lambda x:x[1][1])

    # combine the first and last digit to form a two-digit number
    z = str(sortedtemp[0][1][0]) + str(sortedtemp[-1][1][0])
    
    sum += int(z)

    print(iter, int(z), sum)

    # adds to the sum
    iter +=1


print(f"Sum of all calibratiion values: {sum}")



# answer = 54203