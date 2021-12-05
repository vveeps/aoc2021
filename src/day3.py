from getlines import lines

N_BITS = len(lines[0])


def part1():
    gamma = ""

    for pos in range(N_BITS):
        counts = {
            "0": (n_0 := sum(i[pos] == "0" for i in lines)),
            "1": len(lines) - n_0
        }

        gamma += max(counts, key=lambda i: counts[i])

    return int(gamma, 2) * (int(gamma, 2) ^ (2**N_BITS - 1))


def part2():
    co2_candidates = lines
    o2_candidates = lines
    for pos in range(N_BITS):
        if len(o2_candidates) == len(co2_candidates) == 1:
            break

        co2_zeroes = sum(i[pos] == "0" for i in co2_candidates)
        o2_zeroes = sum(i[pos] == "0" for i in o2_candidates)

        co2_least_common = "0" if co2_zeroes <= len(co2_candidates) / 2 else "1"
        o2_most_common = "0" if o2_zeroes > len(o2_candidates) / 2 else "1"

        if len(o2_candidates) > 1:
            o2_candidates = list(filter(
                lambda number: number[pos] == o2_most_common,
                o2_candidates
            ))

        if len(co2_candidates) > 1:
            co2_candidates = list(filter(
                lambda number: number[pos] == co2_least_common,
                co2_candidates
            ))

    print(f"{o2_candidates = }")
    print(f"{co2_candidates = }")
    return int(o2_candidates[0], 2) * int(co2_candidates[0], 2)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
