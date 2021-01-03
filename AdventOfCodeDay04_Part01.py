import re

raw_input = open("AdventOfCodeDay04.txt","r")
passports = raw_input.read()
passportsList = passports.split("\n\n")
numOfValidPassport = 0
for passport in passportsList:
    passport = passport.replace("\n", " ")

    res = re.findall(r"\s*(byr\s*:\s*(?:19[2-9][0-9]|200[0-2])(?:\s|$)|iyr\s*:\s*20([0-1][0-9]|20)(\s|$)|eyr\s*:\s*20(2[0-9]|30)(\s|$)|hgt\s*:\s*((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)(\s|$)|hcl\s*:\s*#[0-9a-f]{6}(\s|$)|ecl\s*:\s*(amb|blu|brn|gry|grn|hzl|oth)(\s|$)|pid\s*:\s*\d{9}(\s|$))",passport)
    if len(res) < 7:  # Invalid Passport 
        continue

    numOfValidPassport += 1
raw_input.close()
print(f"Num of valid passport = {numOfValidPassport}")