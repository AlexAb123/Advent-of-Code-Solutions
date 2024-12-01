from pathlib import Path
import hashlib
lines = Path(__file__).with_name('Day 05 Input.txt').open('r').read().strip().split("\n")

print(lines)