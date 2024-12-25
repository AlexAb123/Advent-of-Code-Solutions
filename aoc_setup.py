import os
from pathlib import Path

files_created = 0

# Create the Year Directory
year = input("Enter year:\n")
path = Path(__file__).with_name("aoc_" + year)
if not os.path.exists(path):
    path.mkdir()

for day in (map(str, range(1, 26))):

    if len(day) == 1:
        day = "0" + day
    
    # Create the Code Files
    path = Path(__file__).with_name("aoc_" + year) / f"day_{day}.py"
    if not os.path.exists(path):
        with path.open("w") as file:
            file.write(
                f"from pathlib import Path\n"
                f"lines = Path(__file__).with_name('day_{day}_input.txt').open('r').read().strip().split(\"\\n\")\n\n"
                f"print(lines)\n\n"
            )
        print(f"Created file: day {day}.py")
        files_created += 1

    # Create the input Files
    path = Path(__file__).with_name("aoc_" + year) / f"day_{day}_input.txt"
    if not os.path.exists(path):
        with path.open("w") as file:
            pass
        print(f"Created file: day_{day}_input.txt")
        files_created += 1

print(f"Created {files_created} file.") if files_created == 1 else print(f"Created {files_created} files.")