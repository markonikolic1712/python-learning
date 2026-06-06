student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

sum_fun_result = sum(student_scores)
min_fun_result = min(student_scores)
max_fun_result = max(student_scores)

total = 0
min_value = student_scores[0]
max_value = student_scores[0]
for value in student_scores:
    total += value
    if value < min_value:
        min_value = value
    if value > max_value:
        max_value = value

print(f"for loop total: {total}")
print(f"total_sum_fun: {sum_fun_result}")

print(f"for loop min_value: {min_value}")
print(f"min_fun_result: {min_fun_result}")

print(f"for loop max_value: {max_value}")
print(f"max_fun_result: {max_fun_result}")
