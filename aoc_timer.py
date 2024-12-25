import importlib
from time import time

total_time = 0
total_days = 0
year = input("Enter Year:\n")

for day in (map(str, range(1, 26))):

	if len(day) == 1:
		day = "0" + day
		
	# Import each file and measure time taken
	try:
		module = importlib.import_module(f"aoc_{year}.day_{day}")
		start = time()
		module.solve()
		end = time()
		total_time += end - start
		print(f"day_{day}: {int((end - start)*100000)/100} ms")
		total_days += 1
	except ModuleNotFoundError:
		print(f"day_{day}.py not found")
	except AttributeError:
		print(f"day_{day}.py does not have function 'solve'")
		
print(f"Total time taken for {f"{total_days} days" if total_days != 1 else "1 day"}: {int(total_time*100000)/100} ms")
