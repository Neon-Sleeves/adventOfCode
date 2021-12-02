controls = open("day2input.txt", "r")
depth = 0
horizontal = 0
aim = 0

for line in controls:
  print(f'cycled {line}')
  if "down" in line:
    try:
      aim += int(line[-2])
    except ValueError:
      aim += int(line[-1])
  elif "up" in line:
    try:
      aim -= int(line[-2])
    except ValueError:
      aim -= int(line[-1])
  elif "forward" in line:
    try:
      horizontal += int(line[-2])
      depth += int(line[-2]) * aim
    except ValueError:
      horizontal += int(line[-1])
      depth += int(line[-1]) * aim
controls.close()

print(depth)
print(horizontal)
print(aim)
print(depth * horizontal)
