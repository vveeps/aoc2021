from getlines import lines


def part1():
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

    return depth * position


def part2():
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

    return depth * position


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
