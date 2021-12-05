with open("inputs/day1", "r") as f:
    lines = f.read().splitlines()

count = 0
previous = float("inf")

for line in lines:
    if (depth := int(line)) > previous:
        count += 1
    previous = depth

print(f"Measurements larger than previous: {count}")
