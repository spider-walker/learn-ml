highest = 0
current = 0
with open('./data/input0101.txt') as f:
    lines = f.readlines()

for line in lines:
    if not line.strip().isnumeric():
        if current > highest:
            highest = current
        current = 0
    else:
        current += int(line)


print(highest)
