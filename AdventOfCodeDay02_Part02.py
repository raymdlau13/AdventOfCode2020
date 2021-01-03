import re

passwdFile = open("AdventOfCodeDay02.txt","r")
validPasswd = 0
for line in passwdFile:
    m = re.match(r"(\d+)\s*\-(\d+)\s*([a-zA-Z])\s*\:\s*(\S+)", line)
    minOccurrance = int(m.group(1))
    maxOccurrance = int(m.group(2))
    mustHaveChar = m.group(3)
    passwdToBeChecked = m.group(4)
    if ((passwdToBeChecked[minOccurrance-1] == mustHaveChar) != (passwdToBeChecked[maxOccurrance-1] == mustHaveChar)):
        validPasswd += 1
        print(f"Valid Password: {passwdToBeChecked} \t\t{minOccurrance},{maxOccurrance},{mustHaveChar} - {passwdToBeChecked[minOccurrance-1]},{passwdToBeChecked[maxOccurrance-1]}")
print(f"Total number of valid password: {validPasswd}")

