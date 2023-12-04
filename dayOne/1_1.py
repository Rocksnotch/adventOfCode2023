import re

inputStrings = []
newDigits = []
answer = 0

f = open("input1.txt", "r")
for line in f:
    inputStrings.append(line.strip())
f.close()

for string in inputStrings:
    x = re.findall("\d", string)
    if len(x) == 1:
        newDigits.append(int(x[0] + x[0]))
    else:
        newDigits.append(int(x[0] + x[-1]))
            
for num in newDigits:
    answer += num
    
print(answer)