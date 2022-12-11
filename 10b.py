import sys

x = 1
pixels = ''

def lit_pixel(cycle, x):
    y = cycle % 40
    if y == x-1 or y == x or y == x+1:
        return '#'
    return '.'

for line in sys.stdin:
    pixels += lit_pixel(len(pixels), x)
    if line.strip() == 'noop':
        continue
    else:
        val = int(line.strip().split()[1])
        pixels += lit_pixel(len(pixels), x)
        x += val

length = 40
lines = [pixels[i:length+i] for i in range(0, len(pixels), length)]
print('\n'.join(lines))
