signal,cycle,score = 1,1,0
for row in open("Day10_input.txt").read().split("\n"):
    cycleLen = (row != "noop") + 1

    for _ in range(cycleLen):
        if (cycle % 40 - 2) <= signal <= (cycle % 40):
            print("#", end="")
        else:
            print(".", end="")
        if cycle in [20,60,100,140,180,220]:
            score += signal*cycle
        cycle += 1
        if (cycle-1) % 40 == 0:
            print()


    if row != "noop":
        signal += int(row[5:])
print(score)