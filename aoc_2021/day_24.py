from pathlib import Path
lines = Path(__file__).with_name('day_24_input.txt').open('r').read().strip().split("\n")

for line in lines:
    print(line)
