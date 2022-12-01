f = open("Day01_input.txt", "r")
calories = []
personal_calories = []
for row in f:
    if row != "\n":
        personal_calories.append(int(row.strip()))
    else:
        calories.append(personal_calories)
        personal_calories = []
results = [sum(personal) for personal in calories]
print(max(results)) # part 1
print(sum(sorted(results,reverse=True)[:3])) # part 2
