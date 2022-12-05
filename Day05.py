stackText, instructions = open("Day05_input.txt").read().split("\n\n")
rows = stackText.split("\n")
stackDict = {i: [] for i in range(1,10)}
stackIndexes = [rows[-1].index(str(i)) for i in range(1, 10)]

for row in rows[-2::-1]:
    for stack,index in enumerate(stackIndexes):
        if index < len(row) and row[index] != " ":
            stackDict[stack+1].append(row[index])

for row in instructions.split("\n"):
    nOfCreates = int(row[row.index("move") + 5:row.index(" from")])
    fromStack = int(row[row.index("from") + 5:row.index(" to")])
    toStack = int(row[row.index("to") + 3:])
    stackDict[toStack] += stackDict[fromStack][-nOfCreates:] # part 2
    # stackDict[toStack] += stackDict[fromStack][:-nOfCreates-1:-1] # part 1
    stackDict[fromStack] = stackDict[fromStack][:-nOfCreates]

print("".join([stackDict[i][-1] for i in stackDict]))