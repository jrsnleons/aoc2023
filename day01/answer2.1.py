f = open("./finalpuzzle.txt", "r")

num = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}

sum = 0

for line in f:    
    temp = []
    
    # replace word numbers to digits
    for i in num:
        line = line.replace(i, num[i])
    
    # get all digit
    for i in line:
        if i.isdigit():
            temp.append(i)
            
    z = temp[0] + temp[-1]
    print(z)    
    sum += int(z)

print(f'Sum of all calibratioin values: {sum}')
