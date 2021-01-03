lines = [int(line.strip()) for line in open("AdventOfCodeDay01.txt",'r')]
k = 2020
for i in range(0,len(lines)):
    if k - lines[i] in lines[i+1:]:
        print(f"{lines[i]},{k-lines[i]} = {lines[i]*(k-lines[i])}")

