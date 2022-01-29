__hdr__ = '''
### Resistor Picker | v0.9 ##########
### Wolf van der Hert | 07 Jan 2022 #
### https://github.com/Woflje #######
'''
print(__hdr__,"\n")

print("Reading settings.txt")
text_file = open("settings.txt","r")
text_file_data = text_file.read().split("\n")
desired_r = eval(text_file_data[1])
text_file.close()

max_nr = 5

marge = 6

print(f"Desired resistance: {desired_r}\n\nAvailable resistors:\n")

resistors = []

for line in text_file_data[4:]:
	resistance=eval(line)
	resistors.append(resistance)
	print(resistance)

use_resistors = []
print("\n\nPossible combinations:\n")
for r in resistors:
	if r<desired_r:
		use_resistors.append(r)
closest = 999
for r1 in use_resistors:
	for r2 in use_resistors:
		curr_r = r1+r2
		curr_abs = abs(curr_r-desired_r)
		if curr_abs<=closest:
			closest=curr_abs
			print(f"2: {r1}, {r2}, = {curr_r}   delta = {curr_abs}")
		if r1+r2 < desired_r:
			for r3 in use_resistors:
				curr_r = r1+r2+r3
				curr_abs = abs(curr_r-desired_r)
				if curr_abs<=closest:
					closest=curr_abs
					print(f"3: {r1}, {r2}, {r3}, = {curr_r}   delta = {curr_abs}")
				if r1+r2+r3 < desired_r:
					for r4 in use_resistors:
						curr_r = r1+r2+r3+r4
						curr_abs = abs(curr_r-desired_r)
						if curr_abs<=closest:
							closest=curr_abs
							print(f"4: {r1}, {r2}, {r3}, {r4}, = {curr_r}   delta = {curr_abs}")
						if r1+r2+r3+r4 > desired_r:
							for r5 in use_resistors:
								curr_r = r1+r2+r3+r4+r5
								curr_abs = abs(curr_r-desired_r)
								if curr_abs<=closest:
									closest=curr_abs
									print(f"5: {r1}, {r2}, {r3}, {r4}, {r5}, = {curr_r}   delta = {curr_abs}")

input("Press input to close...")