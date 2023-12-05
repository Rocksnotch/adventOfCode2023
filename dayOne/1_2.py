import re

numberWord = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numberNum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
inputArray = []
inputStrings = []
answer = 0

f = open("input1.txt", "r")
for line in f:
    inputStrings.append(line.strip())
f.close()

for i in inputStrings:
    for idx, j in enumerate(numberWord):
        results = re.finditer(j, i)
        for obj in results:
            inputArray.append([numberNum[idx], obj.start()])
            
    x = re.finditer("\d", i)
    for obj in x:
        inputArray.append([int(i[obj.start()]), obj.start()])
        
    inputArray.sort(key=lambda x: x[1])
    temp = str(inputArray[0][0]) + str(inputArray[-1][0])
    answer += int(temp)
    inputArray = []
print(answer)