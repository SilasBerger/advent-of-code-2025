def calc_position(current_position, direction, value):
    if direction == 'L':
        return (current_position - value) % 100
    elif direction == 'R':
        return (current_position + value) % 100
    else:
        raise Exception(f'Unexpected direction: {direction}')
    

with open("input.txt") as f:
    lines = [[line[0], int(line[1:-1])] for line in f.readlines()]

position = 50
zero_count = 0
for line in lines:
    position = calc_position(position, line[0], line[1])
    if position == 0:
        zero_count += 1

print(f'Zero count: {zero_count}')
