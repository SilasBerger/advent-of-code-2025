import re


def is_fake(candidate):
    chars = str(candidate)
    for i in range(len(chars)//2):
        if re.match(f'^({chars[:i+1]})' + '{2,}$', chars) is not None:
            return True


with open('input.txt', 'r') as f:
    raw_ranges = f.readline().split(',')
    ranges = []
    for rr in raw_ranges:
        ranges.append([int(part) for part in rr.split('-')])

sum = 0
for r in ranges:
    for candidate in range(r[0], r[1] + 1):
        if is_fake(candidate):
            sum += candidate
        
print(sum)
