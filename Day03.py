score = 0
score2 = 0
trio = []
for row in open("Day03_input.txt", "r"):
    trio.append(row)
    firstpart, secondpart = row[:len(row) // 2], row[len(row) // 2:]
    for char in firstpart:
        if char in secondpart:
            if char.islower():
                score += ord(char) - ord('a')+1
            else:
                score += ord(char) - ord('A') + 27
            break
    if len(trio) == 3:
        for char in trio[0]:
            if char in trio[1] and char in trio[2]:
                if char.islower():
                    score2 += ord(char) - ord('a') + 1
                else:
                    score2 += ord(char) - ord('A') + 27
                break
        trio = []
print(score)
print(score2)