f = open("Day02_input.txt", "r")
win = {
    "X":"C",
    "Y":"A",
    "Z":"B",
}
inverted_win = {v: k for k, v in win.items()}
draw = {
    "X":"A",
    "Y":"B",
    "Z":"C",
}
inverted_draw = {v: k for k, v in draw.items()}
lose = {
    "X":"B",
    "Y":"C",
    "Z":"A",
}
inverted_lose = {v: k for k, v in lose.items()}

score = 0
part2Score = 0
for row in f:
    result = row.strip().split()
    indeks = list(win.keys()).index(result[1])
    score += indeks + 1
    if result[1] == "Z":
        part2Score += 6
        part2Score += list(win.keys()).index(inverted_win[result[0]])+1
    elif result[1] == "Y":
        part2Score += 3
        part2Score += list(win.keys()).index(inverted_draw[result[0]])+1
    elif result[1] == "X":
        part2Score += list(win.keys()).index(inverted_lose[result[0]])+1
    if ord(result[0])-ord("A") == indeks:
        score += 3
    elif win[result[1]] == result[0]:
        score += 6


print(score)
print(part2Score)