with open("inputs/day2.txt", "r") as f:
    lines = f.read().splitlines()

aim = 0
depth = 0
position = 0

for line in lines:
    command, x = line.split()
    x = int(x)

    if command == "forward":
        position += x
        depth += aim * x
    elif command == "up":
        aim -= x
    else:  # down
        aim += x

print(f"{depth * position = }")
