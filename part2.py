# Part 2 of the Python Review lab.

def encode(x, y):
	if 1<y<250 and 500<x<1000:
		print(x * y)
	else:
		print("Invalid input: Outside range")
		print("none")

def decode(coded_message):
	pass


encode(100, 700)
