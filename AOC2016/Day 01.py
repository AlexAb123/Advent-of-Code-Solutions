from pathlib import Path
lines = Path(__file__).with_name('Day 01 Input.txt').open('r').read().strip().split(", ")

# Turning right adds one to the index mod 4
# Turning right removes one from the index mod 4
# up, right, down, left
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
direction = 0
visited = set()
part2_found = False
pos = [0, 0]
part2 = 0
for line in lines:
    if line[0] == "R":
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    if part2_found:
        pos[0] += int(line[1:]) * directions[direction][0]
        pos[1] += int(line[1:]) * directions[direction][1]
    else:
        for i in range(int(line[1:])):
            pos[0] += directions[direction][0]
            pos[1] += directions[direction][1]
            if tuple(pos) in visited:
                part2 = abs(pos[0]) + abs(pos[1])
                part2_found = True
            visited.add(tuple(pos))

print(f"Part 1: {abs(pos[0]) + abs(pos[1])}")
print(f"Part 2: {part2}")