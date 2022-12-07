inp = open("Day06_input.txt").read()
print([indeks+4 for indeks in range(len(inp)) if len(set(inp[indeks:indeks+4])) == 4][0]) # part 1
print([indeks+14 for indeks in range(len(inp)) if len(set(inp[indeks:indeks+14])) == 14][0]) # part 2