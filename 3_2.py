import re


def calculate_sum_of_multiplications(data):
    mul_pattern = r"mul\((\d+),(\d+)\)"
    control_pattern = r"do\(\)|don\'t\(\)"

    total_sum = 0
    enabled = True

    controls = re.finditer(control_pattern, data)
    muls = re.finditer(mul_pattern, data)

    controls = list(controls)
    muls = list(muls)

    control_index = 0
    mul_index = 0

    while control_index < len(controls) or mul_index < len(muls):
        next_control = (
            controls[control_index] if control_index < len(controls) else None
        )
        next_mul = muls[mul_index] if mul_index < len(muls) else None

        if next_control and (
            not next_mul or next_control.start() < next_mul.start()
        ):  # noqa
            if next_control.group() == "do()":
                enabled = True
            elif next_control.group() == "don't()":
                enabled = False
            control_index += 1
        elif next_mul:
            if enabled:
                x, y = map(int, next_mul.groups())
                total_sum += x * y
            mul_index += 1

    return total_sum


file_path = "./data/3/input.txt"
with open(file_path, "r") as file:
    data = file.read()

result = calculate_sum_of_multiplications(data)
print(result)
