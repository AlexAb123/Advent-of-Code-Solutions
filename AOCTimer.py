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
		print(f"Day {day}:")
		module = importlib.import_module(f"AOC{year}.Day {day}")
		start = time()
		module.solve()
		end = time()
		print(f"Time Taken: {int((end - start)*100000)/100} ms\n")
		total_time += end - start
		total_days += 1
	except ModuleNotFoundError:
		print(f"Day {day}.py not found\n")
	except AttributeError:
		print(f"Day {day}.py does not have function 'solve'\n")
		
print(f"Total time taken for {f"{total_days} days" if total_days != 1 else "1 day"}: {int(total_time*100000)/100} ms")