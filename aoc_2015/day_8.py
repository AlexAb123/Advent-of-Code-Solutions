from pathlib import Path
lines = Path(__file__).with_name('day 8 input.txt').open('r').read().strip().split("\n")


part1 = 0
for line in lines:
    print(line)
    line.replace(r"\"", "A")
    part1 -= line.count(r"\x")
    line.replace(r"\x", "")
    line.replace("\"", "")
    print(line)
    part1 += len(line)
print(part1)