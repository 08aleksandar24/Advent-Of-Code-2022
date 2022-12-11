folderSizes = {}
path = ""
for line in open("Day07_input.txt").read().split("\n"):
    if "$ cd /" in line:
        path = "/"
    elif line == "$ cd ..":
        path = "/".join(path.split("/")[:-2])+"/"
    elif "$ cd" in line:
        path += line[5:] + "/"
    elif "$" not in line:
        typeOrSize, name = line.split()
        if typeOrSize != "dir":
            i = 0
            while "/" in path[i:]:
                i += path[i:].index("/") + 1
                if path[:i] in folderSizes:
                    folderSizes[path[:i]] += int(typeOrSize)
                else:
                    folderSizes[path[:i]] = int(typeOrSize)
print(sum([folderSizes[folder] for folder in folderSizes if folderSizes[folder]<100000])) # part 1
print(min([folderSizes[folder] for folder in folderSizes if 70000000-folderSizes["/"]+folderSizes[folder]>30000000])) # part 2

