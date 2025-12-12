with open('../inputs/day03.txt') as f:
    banks = [bank.strip() for bank in f.readlines()]

sum = 0
for bank in banks:
    d10 = 0
    d10_pos = 0
    d1 = 0
    for idx, joltage in enumerate(bank[:-1]):
        if int(joltage) > d10:
            d10 = int(joltage)
            d10_pos = idx
    for joltage in bank[d10_pos + 1:]:
        if int(joltage) > d1:
            d1 = int(joltage)
    sum += int(f'{d10}{d1}')

print(sum)