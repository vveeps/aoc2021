with open("inputs/day2.txt", "r") as f:
    lines = f.read().splitlines()

depth = 0
position = 0

for line in lines:
    command, x = line.split()
    x = int(x)

    if command == "forward":
        position += x
    elif command == "up":
        depth -= x
    else:  # down
        depth += x

print(f"{depth * position = }")
