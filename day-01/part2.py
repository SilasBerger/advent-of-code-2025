def calc_position(current_position, direction, value):
    if direction == 'L':
        new_position = (current_position - value) % 100
        zeros = abs((current_position - value) // 100)
        if current_position == 0:  # (0-50)//100 = -1, but we've already counted that 0 when we got to it.
            zeros -= 1
        if new_position == 0:  # (50-50)//100 = 0, but we need to count this one
            zeros += 1
        return new_position, zeros
    elif direction == 'R':
        new_position = (current_position + value) % 100
        zeros = (current_position + value) // 100
        return new_position, zeros
    else:
        raise Exception(f'Unexpected direction: {direction}')
    

with open("input.txt") as f:
    lines = [[line[0], int(line[1:-1])] for line in f.readlines()]

position = 50
zero_count = 0
for line in lines:
    new_position, new_zeros = calc_position(position, line[0], line[1])
    position = new_position
    zero_count += new_zeros

print(f'Zero count: {zero_count}')