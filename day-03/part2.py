REQUIRED_BATTERIES = 12  # Use 2 for solution to part 1

with open('input.txt') as f:
    banks = [bank.strip() for bank in f.readlines()]

batteries_per_bank = len(banks[0])

sum = 0
for bank in banks:
    bank = [int(b) for b in bank]
    selected_batteries = []
    predecessor_idx = -1
    for batt_idx in range(REQUIRED_BATTERIES):
        highest_joltage = 0
        max_idx = batteries_per_bank - REQUIRED_BATTERIES + batt_idx
        for idx in range(predecessor_idx + 1, max_idx + 1):
            joltage = bank[idx]
            if joltage > highest_joltage:
                highest_joltage = joltage
                predecessor_idx = idx
        selected_batteries.append(highest_joltage)
    sum += int(''.join([str(b) for b in selected_batteries]))

print(sum)