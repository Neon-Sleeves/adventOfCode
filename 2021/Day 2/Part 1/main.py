controls = open("day2input.txt", "r")
depth = 0
horizontal = 0

for line in controls:
  print(f'cycled {line}')
  if "down" in line:
    try:
      depth += int(line[-2])
    except ValueError:
      depth += int(line[-1])
  elif "up" in line:
    try:
      depth -= int(line[-2])
    except ValueError:
      depth -= int(line[-1])
  elif "forward" in line:
    try:
      horizontal += int(line[-2])
    except ValueError:
      horizontal += int(line[-1])
controls.close()

print(depth)
print(horizontal)
print(depth * horizontal)
