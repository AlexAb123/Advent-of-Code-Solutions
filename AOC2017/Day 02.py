from pathlib import Path
lines = [list(map(int, line.split("\t"))) for line in Path(__file__).with_name('Day 02 Input.txt').open('r').read().strip().split("\n")]

print(f"Part 1: {sum(map(lambda line: max(line) - min(line), lines))}")

part2 = 0
for line in lines:
    found = False
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            if line[i] % line[j] == 0:
                part2 += line[i]//line[j]
                found = True
                break
            elif line[j] % line[i] == 0:
                part2 += line[j]//line[i]
                found = True
                break
        if found:
            break
print(f"Part 2: {part2}")