from pathlib import Path
lines = Path(__file__).with_name('Day 01 Input.txt').open('r').read().strip().split("\n")

total = 0
part1 = 0
part2 = 0
found = False
cycle_done = False
seen = set()
i = 0
while not found or not cycle_done:
    line = lines[i]
    sign = line[0]
    number = int(line[1:])
    if sign == "+":
        total += number
    else:
        total -= number
    if total in seen and not found:
        part2 = total
        found = True
    seen.add(total)
    if i < len(lines) - 1:
        i += 1
    else:
        if not cycle_done:
            part1 = total
            cycle_done = True
        i = 0
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")