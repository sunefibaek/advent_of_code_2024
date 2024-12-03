def calculate_similarity_score_from_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    left_list = []
    right_list = []
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    from collections import Counter

    right_count = Counter(right_list)

    similarity_score = 0
    for left in left_list:
        similarity_score += left * right_count[left]

    return similarity_score


file_path = "./data/1/input.txt"

similarity_score = calculate_similarity_score_from_file(file_path)
print(similarity_score)
