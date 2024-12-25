from pathlib import Path
import hashlib
lines = Path(__file__).with_name('day 05 input.txt').open('r').read().strip().split("\n")

print(lines)