from pathlib import Path
lines1 = [list(map(int, filter(lambda x: x != "", line.split(" ")))) for line in Path(__file__).with_name('Day 03 Input.txt').open('r').read().strip().split("\n")]
lines2 = [sorted([lines1[r][c], lines1[r+1][c], lines1[r+2][c]]) for r in range(0, len(lines1)-2, 3) for c in range(3)]
lines1 = map(sorted, lines1)
print(f"Part 1: {sum(map(lambda x: int(x[0] + x[1] > x[2]), lines1))}")
print(f"Part 2: {sum(map(lambda x: int(x[0] + x[1] > x[2]), lines2))}")