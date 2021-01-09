import re

def recursive_count(all_bags,current_bag):
    count = 1
    for k, v in all_bags[current_bag].items():
        multiplier = v
        count += multiplier * recursive_count(all_bags,k)
    return count

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

bag_to_find = 'shiny gold'
found_bags = recursive_count(bag_collection, bag_to_find ) - 1
print(f"{found_bags} bags can contain {bag_to_find}.")