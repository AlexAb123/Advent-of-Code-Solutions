from pathlib import Path
lines = Path(__file__).with_name('17_Input.txt').open('r').read().strip().split("\n")

for line in lines:
    print(line)
