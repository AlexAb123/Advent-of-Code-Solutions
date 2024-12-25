from pathlib import Path
lines = Path(__file__).with_name('day_25_input.txt').open('r').read().strip().split("\n")

rows, cols = len(lines), len(lines[0])

east_cucumbers = set()
south_cucumbers = set()

for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == ">":
            east_cucumbers.add((r,c))
        elif lines[r][c] == "v":
            south_cucumbers.add((r,c))

step = 0
moves = -1

def vis(east, south):
    g = [["." for _ in range(cols)] for _ in range(rows)]
    for r,c in east:
        g[r][c] = ">"
    for r,c in south:
        g[r][c] = "v"
    for l in g:
        print("".join(l))

while moves != 0:
    vis(east_cucumbers, south_cucumbers)

    moves = 0

    new_east_cucumbers = east_cucumbers.copy()
    for pos in east_cucumbers:

        if (pos[0], pos[1]+1) in east_cucumbers or (pos[0], pos[1]+1) in south_cucumbers:
            new_east_cucumbers.add(pos)
            continue

        if pos[1]+1 >= cols and (pos[0], (pos[1]+1)%cols) in east_cucumbers or (pos[0], (pos[1]+1)%cols) in south_cucumbers:
            new_east_cucumbers.add(pos)
            continue

        moves += 1
        new_east_cucumbers.remove(pos)
        new_east_cucumbers.add((pos[0], (pos[1]+1)%cols))

    east_cucumbers = new_east_cucumbers.copy()

    new_south_cucumbers = south_cucumbers.copy()
    for pos in south_cucumbers:

        if (pos[0], pos[1]+1) in east_cucumbers or (pos[0], pos[1]+1) in south_cucumbers:
            new_south_cucumbers.add(pos)
            continue

        if pos[0]+1 >= rows and ((pos[0]+1)%rows, pos[1]) in east_cucumbers or ((pos[0]+1)%rows, pos[1]) in south_cucumbers:
            new_south_cucumbers.add(pos)
            continue

        moves += 1
        new_south_cucumbers.remove(pos)
        new_south_cucumbers.add(((pos[0]+1)%rows, pos[1]))

    south_cucumbers = new_south_cucumbers.copy()
    if step == 10:
        break
    print(step)
    step += 1

print(step)