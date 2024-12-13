from pathlib import Path
lines = list(map(int, Path(__file__).with_name('01_Input.txt').open('r').read().strip().split("\n")))

part1Score = 0
part2Score = 0
for i in range(len(lines)-1):
    if lines[i] < lines[i+1]:
        part1Score += 1
    # The middle two lines of the sum are the same. Only have to compare the first line of the first sum and the last line of the last sum
    if i+3 < len(lines) and lines[i] < lines[i+3]:
        part2Score += 1
print(f"Part 1: {part1Score}")
print(f"Part 2: {part2Score}")