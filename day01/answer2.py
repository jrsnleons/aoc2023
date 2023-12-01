f = open("./dum.txt", "r")

sum = 0

# dictionary of numbers in words
numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

for x in f:
    
    # temp = {key(value+position): value, position}
    temp = {}
    
    # checks if there are digits and adds to dict
    for a, y in enumerate(x):
        print(a, " ", y, " ", y.isalpha())
        if y.isalpha() or y == "\n":
            pass
        else:
            print("y")
            temp[y] = a
            print("temp: ", temp[y])

    #checks if there are sub string numbers and adds to dict
    for u in numbers:
        if x.find(u) != -1:
            temp[str(numbers[u])] = x.find(u)
    
    # sorts the dict by their positions
    sortedtemp = sorted(temp.items(), key=lambda x:x[1])
    print(sortedtemp)

    # combine the first and last digit to form a two-digit number
    z = sortedtemp[0][0] + sortedtemp[-1][0]
    
    print(z)
    
    # adds to the sum
    sum += int(z)
    

print(f"Sum of all calibratiion values: {sum}")

# 4vzpsdreight337hgvq
# jone4ccn8
# nftdkmtmcz4
# nlnineeightmndkqz8nineonenrqm
# nrhdxfsqvxcbcghf35eightthreeseven5