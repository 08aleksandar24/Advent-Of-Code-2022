import numpy as np
map = [line for line in open("Day08_input.txt").read().split("\n")]
visible = np.zeros((len(map),len(map[0])))
bestScore = 0
for i in range(1,len(map)-1):
    for j in range(1, len(map[i]) - 1):
        if max(map[i][:j])<map[i][j]:
            visible[i][j] = 1
        if max([map[k][j] for k in range(i)])<map[i][j]:
            visible[i][j] = 1
        if max(map[i][j+1:])<map[i][j]:
            visible[i][j] = 1
        if max([map[k][j] for k in range(i+1,len(map[i]))])<map[i][j]:
            visible[i][j] = 1

        up = 0
        for k in range(i - 1, -1, -1):
            up += 1
            if map[i][j] <= map[k][j]:
                break

        down = 0
        for k in range(i + 1, len(map)):
            down += 1
            if map[i][j] <= map[k][j]:
                break

        left = 0
        for k in range(j - 1, -1, -1):
            left += 1
            if map[i][j] <= map[i][k]:
                break

        right = 0
        for k in range(j + 1, len(map[i])):
            right += 1
            if map[i][j] <= map[i][k]:
                break

        score = up*down*left*right
        if score > bestScore:
            bestScore = score
print(np.sum(visible)+2*len(map)+2*len(map[0])-4)
print(bestScore)