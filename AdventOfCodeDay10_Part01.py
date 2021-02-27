

if __name__ == "__main__":
    adapters = [int(joltage.strip()) for joltage in open("AdventOfCodeDay10.txt","r")]
    print(f"{adapters}")
    max_adapter_joltage = max(adapters)

    current_joltage = 0
    adapter_combination = []
    diff_of_one_joltage = 0
    diff_of_two_joltage = 0
    diff_of_three_joltage = 1
    while current_joltage < max_adapter_joltage:
        if current_joltage + 1 in adapters:
            diff_of_one_joltage += 1
            adapter_combination.append(current_joltage+1)
        elif current_joltage + 2 in adapters:
            diff_of_two_joltage += 1
            adapter_combination.append(current_joltage+2)
        elif current_joltage + 3 in adapters:
            diff_of_three_joltage += 1
            adapter_combination.append(current_joltage+3)
        else:
            break
        current_joltage = adapter_combination[-1]
    print(adapter_combination)
    print(f"{diff_of_one_joltage} differences of one jolt.")
    print(f"{diff_of_two_joltage} differences of two jolts.")
    print(f"{diff_of_three_joltage} differences of three jolts.")
    print(f"result = {diff_of_one_joltage*diff_of_three_joltage}")


