import os
from pathlib import Path

files_created = 0

# Create the Year Directory
year = input("Enter year:\n")
path = Path(__file__).with_name("AOC" + year)
if not os.path.exists(path):
    path.mkdir()

for day in (map(str, range(1, 26))):

    if len(day) == 1:
        day = "0" + day
    
    # Create the Code Files
    path = Path(__file__).with_name("AOC" + year) / f"Day_{day}.py"
    if not os.path.exists(path):
        with path.open("w") as file:
            file.write(
                f"from pathlib import Path\n"
                f"lines = Path(__file__).with_name('Day_{day}_Input.txt').open('r').read().strip().split(\"\\n\")\n\n"
                f"print(lines)\n\n"
            )
        print(f"Created file: Day {day}.py")
        files_created += 1

    # Create the Input Files
    path = Path(__file__).with_name("AOC" + year) / f"Day_{day}_Input.txt"
    if not os.path.exists(path):
        with path.open("w") as file:
            pass
        print(f"Created file: Day {day} Input.txt")
        files_created += 1

print(f"Created {files_created} file.") if files_created == 1 else print(f"Created {files_created} files.")