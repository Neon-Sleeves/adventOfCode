lines = []
bitsByPos = [[],[],[],[],[],[],[],[],[],[],[],[],[]]

def start(inputFile):
  txt = open(inputFile, "r")
  # sorter
  for line in txt:
    index = 0
    lines.append(line[:-1])
    for bit in line:
      bitsByPos[index].append(bit)
      index += 1

  # cleaning lists
  bitsByPos.remove(bitsByPos[len(bitsByPos)-1])
  txt.close()



start("day3input.txt")
# then add checker for consider that leads into lines in loop that narrows
def oxy():
  consider = lines.copy()
  iterateBitPos = bitsByPos.copy()
  bitPos = 0
  for i in iterateBitPos:
    iterate = consider.copy()
    if iterateBitPos[bitPos].count('1') >= iterateBitPos[bitPos].count('0'):
      for line in iterate:
        if line[bitPos] == '0':
          consider.remove(line)
          #
    elif iterateBitPos[bitPos].count('0') > iterateBitPos[bitPos].count('1'):
      for line in iterate:
        if line[bitPos] == '1':
          consider.remove(line)
          #
    #checking if complete
    if len(consider) == 1:
      break
    #updating bitpos
    for bitList in iterateBitPos:
      bitList.clear()
    for line in consider:
      index = 0
      for bit in line:
        iterateBitPos[index].append(bit)
        index += 1
    #
    bitPos += 1
  return consider

def carb():
  consider = lines.copy()
  iterateBitPos = bitsByPos.copy()
  bitPos = 0
  for i in bitsByPos:
    iterate = consider.copy()
    if bitsByPos[bitPos].count('1') < bitsByPos[bitPos].count('0'):
      for line in iterate:
        if line[bitPos] == '0':
          consider.remove(line)
    elif bitsByPos[bitPos].count('0') <= bitsByPos[bitPos].count('1'):
      for line in iterate:
        if line[bitPos] == '1':
          consider.remove(line)
    if len(consider) == 1:
      break
    #updating bitpos
    for bitList in iterateBitPos:
      bitList.clear()
    for line in consider:
      index = 0
      for bit in line:
        iterateBitPos[index].append(bit)
        index += 1
    #
    bitPos += 1
  return consider

output = open('day3output.txt', 'w')
output.write(f"Oxy: {''.join(oxy())} ")
output.write(f"Carb: {''.join(carb())}")


output.close()
