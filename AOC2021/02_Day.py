from pathlib import Path
lines = Path(__file__).with_name('02_Input.txt').open('r').read().strip().split("\n")

lines = [line.split(" ") for line in lines]
lines = [[line[0], int(line[1])] for line in lines]

depth = 0
x = 0
for line in lines:
    if line[0] == "forward":
        x += line[1]
    elif line[0] == "down":
        depth += line[1]
    elif line[0] == "up":
        depth -= line[1]
print(f"Part 1: {depth*x}")

depth = 0
x = 0
aim = 0
for line in lines:
    if line[0] == "forward":
        x += line[1]
        depth += aim * line[1]
    elif line[0] == "down":
        aim += line[1]
    elif line[0] == "up":
        aim -= line[1]
print(f"Part 2: {depth*x}")