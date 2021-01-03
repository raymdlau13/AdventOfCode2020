
raw_input = open("AdventOfCodeDay06.txt","r")
groups = [raw.replace("\n", " ").split() for raw in raw_input.read().split("\n\n")]
total_answers = 0
total_common_answers = 0
for group in groups:
    group_answers = {}
    for answers in group:
        for answer in answers:
            if answer not in group_answers:
                group_answers[answer] = 1
            else:
                group_answers[answer] += 1
    total_common_answers += len([1 for k,v in group_answers.items() if v == len(group)])
    total_answers += len(group_answers)


print(f"Total Answers: {total_answers}")
print(f"Total Common Answers: {total_common_answers}")