import re

def convert_field_to_dictionary(passport_field_list):
    field_dictionary = {}
    for field in passport_field_list:
        pair = field.split(":")
        field_dictionary[pair[0]] = pair[1]
    return field_dictionary

def is_valid_passport(passport):
    print(passport)
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    has_valid_byr = ( "byr" in passport and re.match(r"^(19[2-9][0-9]|200[0-2])$",passport["byr"]))
    
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    has_valid_iyr = ( "iyr" in passport and re.match(r"^(20(1[0-9]|20))$",passport["iyr"]))
    
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    has_valid_eyr = ( "eyr" in passport and re.match(r"^(20(2[0-9]|30))$",passport["eyr"]))
    
    # hgt (Height) - a number followed by either cm or in:
    #    If cm, the number must be at least 150 and at most 193.
    #    If in, the number must be at least 59 and at most 76.
    has_valid_hgt = ( "hgt" in passport and re.match(r"^(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$",passport["hgt"]))
    
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    has_valid_hcl = ( "hcl" in passport and re.match(r"^#[0-9a-fA-F]{6}$",passport["hcl"]))
    
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    has_valid_ecl = ( "ecl" in passport and re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$",passport["ecl"]))
    
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    has_valid_pid = ( "pid" in passport and re.match(r"^\d{9}$",passport["pid"]))
    
    # cid (Country ID) - ignored, missing or not.
    
    return (
        has_valid_byr and
        has_valid_iyr and
        has_valid_eyr and
        has_valid_hgt and
        has_valid_hcl and
        has_valid_ecl and
        has_valid_pid 
    )

if __name__ == "__main__":
    raw_input = open("AdventOfCodeDay04.txt","r")
    passports_list = [passport.replace("\n", " ").split() for passport in raw_input.read().split("\n\n")]
    passports = [convert_field_to_dictionary(item) for item in passports_list]
    valid_passports = [passport for passport in passports if is_valid_passport(passport)]
    print(len(valid_passports))