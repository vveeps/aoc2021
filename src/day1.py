from getlines import lines


def part1():
    count = 0
    previous = float("inf")

    for line in lines:
        if (depth := int(line)) > previous:
            count += 1
        previous = depth

    return count


def part2():
    count = 0
    previous = float("inf")

    for i in range(len(lines) - 2):
        if (depth_sum := sum(int(depth) for depth in lines[i:i+3])) > previous:
            count += 1
        previous = depth_sum

    return count


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
