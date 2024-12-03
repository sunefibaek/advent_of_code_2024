def calculate_total_distance_from_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    left_list = []
    right_list = []
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    left_list.sort()
    right_list.sort()

    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)

    return total_distance


file_path = "./data/1/input.txt"  # Make sure this path is correct

total_distance = calculate_total_distance_from_file(file_path)
print(total_distance)
