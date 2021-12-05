with open("inputs/day1.txt", "r") as f:
    lines = f.read().splitlines()

count = 0
previous = float("inf")

for i in range(len(lines) - 2):
    if (depth_sum := sum(int(depth) for depth in lines[i:i+3])) > previous:
        count += 1
    previous = depth_sum

print(f"Measurement sums larger than previous: {count}")
