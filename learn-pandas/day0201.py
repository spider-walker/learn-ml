import sys

with open(f'./data/{sys.argv[1]}.txt') as f:
    lines = f.read().splitlines()

print(lines)
