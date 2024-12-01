from pathlib import Path
lines = Path(__file__).with_name('Day 8 Input.txt').open('r').read().strip().split("\n")


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