positions1 = set()
positions9 = set()
rope = [(50,50),(50,50),(50,50),(50,50),(50,50),(50,50),(50,50),(50,50),(50,50),(50,50)]
positions1.add(rope[1])
positions9.add(rope[9])
for row in open("Day09_input.txt").read().split("\n"):
    direction, steps = row.split()
    for _ in range(int(steps)):
        previousRope = rope[0]
        if direction == "D":
            rope[0] = (rope[0][0]+1, rope[0][1])
        if direction == "U":
            rope[0] = (rope[0][0]-1, rope[0][1])
        if direction == "L":
            rope[0] = (rope[0][0], rope[0][1]-1)
        if direction == "R":
            rope[0] = (rope[0][0], rope[0][1]+1)
        for i in range(1,len(rope)):
            if abs(rope[i][0] - rope[i - 1][0]) > 1 or abs(rope[i][1] - rope[i - 1][1]) > 1:
                hor = rope[i - 1][0] - rope[i][0]
                ver = rope[i - 1][1] - rope[i][1]
                if abs(hor) > 0:
                    rope[i] = rope[i][0] + hor // abs(hor), rope[i][1]
                if abs(ver) > 0:
                    rope[i] = rope[i][0], rope[i][1] + ver // abs(ver)




        positions1.add(rope[1])
        positions9.add(rope[9])


print(len(positions1)) # part 1: 6037
print(len(positions9)) # part 2