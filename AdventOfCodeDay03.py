def is_tree_at_coordinate(hill_x, hill_y):
    map_x = hill_x % len(map_basis[hill_y])
    return map_basis[hill_y][map_x] == "#"

def tree_count_for_slope(right_increment,down_increment):
    right_coordinate = 0
    down_coordinate =0
    tree_count = 0
    
    while down_coordinate < len(map_basis):
        if is_tree_at_coordinate(right_coordinate, down_coordinate):
            tree_count += 1
        right_coordinate += right_increment
        down_coordinate += down_increment

    return tree_count

if __name__ == "__main__":
    map_basis = [line.strip() for line in open("AdventOfCodeDay03.txt","r")]

    print(f"Numober of Trees: {tree_count_for_slope(1,1)}")
    print(f"Numober of Trees: {tree_count_for_slope(3,1)}")
    print(f"Numober of Trees: {tree_count_for_slope(5,1)}")
    print(f"Numober of Trees: {tree_count_for_slope(7,1)}")
    print(f"Numober of Trees: {tree_count_for_slope(1,2)}")

    print( \
    tree_count_for_slope(1,1) * \
    tree_count_for_slope(3,1) * \
    tree_count_for_slope(5,1) * \
    tree_count_for_slope(7,1) * \
    tree_count_for_slope(1,2))

