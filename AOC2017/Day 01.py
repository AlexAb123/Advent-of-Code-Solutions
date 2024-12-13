from pathlib import Path
line = [int(c) for c in Path(__file__).with_name('Day 01 Input.txt').open('r').read().strip()]
print(f"Part 1: {sum(map(lambda i: line[i] if line[i] == line[(i+1) % len(line)] else 0, range(len(line))))}")
print(f"Part 2: {sum(map(lambda i: line[i] if line[i] == line[(i+len(line)//2) % len(line)] else 0, range(len(line))))}")

""" part1 = 0
part2 = 0
for i in range(len(line)):
    if line[i] == line[(i+1) % len(line)]:
        part1 += line[i]
    if line[i] == line[(i+len(line)//2) % len(line)]:
        part2 += line[i]
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
 """