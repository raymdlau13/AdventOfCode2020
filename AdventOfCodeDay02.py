import re

if __name__ == "__main__":
    passwdFile = open("AdventOfCodeDay02.txt","r")
    validPasswd = 0
    for line in passwdFile:
        m = re.match(r"(\d+)\s*\-(\d+)\s*([a-zA-Z])\s*\:\s*(\S+)", line)
        minOccurrance = int(m.group(1))
        maxOccurrance = int(m.group(2))
        mustHaveChar = m.group(3)
        passwdToBeChecked = m.group(4)
        numOfOccurrance = passwdToBeChecked.count(mustHaveChar)
        if numOfOccurrance >= minOccurrance and numOfOccurrance <= maxOccurrance:
            validPasswd += 1
            print(f"Valid Password: {passwdToBeChecked} \t\t{minOccurrance},{maxOccurrance},{mustHaveChar}")
    print(f"Total number of valid password: {validPasswd}")


