def is_safe_report(levels):
    n = len(levels)
    if n < 2:
        return True

    increasing = True
    decreasing = True

    for i in range(1, n):
        diff = levels[i] - levels[i - 1]
        if diff < -3 or diff > 3 or diff == 0:
            return False
        if diff > 0:
            decreasing = False
        if diff < 0:
            increasing = False

    return increasing or decreasing


def is_safe_by_removing_one_level(levels):
    n = len(levels)
    if n <= 2:
        return True

    for i in range(n):
        new_levels = levels[:i] + levels[i + 1 :]  # noqa
        if is_safe_report(new_levels):
            return True

    return False


def count_safe_reports_from_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    safe_report_count = 0

    for line in lines:
        levels = list(map(int, line.split()))
        if is_safe_report(levels) or is_safe_by_removing_one_level(levels):
            safe_report_count += 1

    return safe_report_count


file_path = "./data/2/input_validation.txt"

safe_report_count = count_safe_reports_from_file(file_path)
print(f"Number of safe reports: {safe_report_count}")
