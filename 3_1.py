import re


def parse_and_sum_mul_operations_from_file(file_path):
    pattern = r"mul\((\d+),(\d+)\)"
    with open(file_path, "r") as file:
        corrupted_memory = file.read()
    matches = re.findall(pattern, corrupted_memory)
    result_sum = sum(int(x) * int(y) for x, y in matches)
    return result_sum


file_path = "./data/3/input.txt"
result = parse_and_sum_mul_operations_from_file(file_path)
print(result)
