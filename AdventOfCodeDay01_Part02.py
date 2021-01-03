
lines = [int(line.strip()) for line in open("AdventOfCodeDay01.txt","r")]
k1 = 2020
for i in range(0,len(lines)):
    k2 = k1 - lines[i]
    for j in range(i+1,len(lines)):
        if k2 - lines[j] in lines[j+1:]:
            print(f"{lines[i]},{lines[j]},{k2-lines[j]} = {lines[i]*lines[j]*(k2-lines[j])}")