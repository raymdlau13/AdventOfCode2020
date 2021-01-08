import re

def check_bags(all_bags, bag_looking_for, current_bag):
    if bag_looking_for == current_bag:
        return 1
    if all_bags.get(current_bag) is None:
        return 0
    else:
        counts = 0
        for bag, numOfBag in all_bags[current_bag].items():
            counts = ( counts or check_bags(all_bags,bag_looking_for,bag))
        return counts
    
bags = [line.strip() for line in open("AdventOfCodeDay07.txt","r")]
#print(bags)
bag_collection = {}
for bag in bags:
    subBag = {}
    mainBag = re.findall(r"^\s*(\w+\s+\w+)\s+bags\s+contain",bag,re.IGNORECASE)
    sb = re.findall(r"(\d)+\s+(\w+\s+\w+)\s+bag",bag,re.IGNORECASE)
    for eachSubBag in sb:
        if eachSubBag[1] not in subBag:
            subBag[eachSubBag[1]] = int(eachSubBag[0])
    if mainBag[0] not in bag_collection:
        bag_collection[mainBag[0]] = subBag
print(bag_collection)         
found_bags = 0
bag_to_find = 'shiny gold'
for k, v in bag_collection.items():
    if k != bag_to_find:
        found_bags += check_bags(bag_collection,bag_to_find,k)

print(f"{found_bags} bags can contain {bag_to_find}.")