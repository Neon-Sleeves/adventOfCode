txt = open("day3input.txt", "r")
gamma = []
epsilon = []


lines = [[],[],[],[],[],[],[],[],[],[],[],[],[]]

# sorter
for line in txt:
  index = 0
  for bit in line:
    lines[index].append(bit)
    index += 1

# cleaning lines
lines.remove(lines[len(lines)-1])

# gamma calc
for bitList in lines:
  if bitList.count('0') > bitList.count('1'):
    gamma.append('0')
  elif bitList.count('1') > bitList.count('0'):
    gamma.append('1')

# epsilon calc
epsilon = []
for bit in gamma:
  epsilon.append(str(1 - int(bit)))

gamma = ''.join(gamma)
epsilon = ''.join(epsilon)


print(gamma)
print(epsilon)
print(int(gamma, 2) * int(epsilon, 2))

