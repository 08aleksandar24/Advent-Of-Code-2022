contain = 0
overlap = 0
for row in open("Day04_input.txt", "r"):
    pairs = row.split(",")
    section1 = pairs[0].split("-")
    section2 = pairs[1].split("-")
    if max(int(section1[1]),int(section2[1]))-min(int(section1[0]),int(section2[0])) == max(int(section2[1])-int(section2[0]),int(section1[1])-int(section1[0])):
        contain += 1
    if not(int(section1[1])<int(section2[0]) or int(section2[1])<int(section1[0])):
        overlap += 1
print(contain)
print(overlap)