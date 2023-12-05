import re

numberWord = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numberNum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
inputDict = {}
inputStrings = []
answer = 0

f = open("input1.txt", "r")
for line in f:
    inputStrings.append(line.strip())
f.close()

