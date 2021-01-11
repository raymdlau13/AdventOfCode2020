def check_sum(target_sum,preamble):
    found_pair = False
    for num in preamble:
        if target_sum - num in preamble:
            found_pair = True
            break
    return found_pair

def check_xmas(xmas,preamble_len):
    start_point = 0
    for start_point in range(0,len(xmas)-preamble_len):
        if not check_sum(xmas[start_point+preamble_len],xmas[start_point:start_point+preamble_len]):
            print(f"invalid sum {xmas[start_point+preamble_len]}")
            print(f"preamble = {xmas[start_point:start_point+preamble_len]}")
            break
    return 0

if __name__ = "__main__":
    xmas = [int(number.strip()) for number in open("AdventOfCodeDay09.txt","r")]
    check_xmas(xmas,25)