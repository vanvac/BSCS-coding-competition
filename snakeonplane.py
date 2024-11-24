garden = '''╔════════╗
║.;~┌ ┐¸.║
║.┌.:┐;:.║
║ '~~¸::;║
║.¸.,; ¸`║
║~└~~┘ : ║
║:¸¸...`.║
║` '└:┘' ║
║¸,.;':~~║
╚════════╝'''

def splitIntoMultidimList(WeirdString):
  MultidimList = []
  for line in WeirdString.split('\n'):
    MultidimList.append(list(line))
  return MultidimList


def findBox(multiDimList):
  boxIndexList = []
  for x,  layer in enumerate(multiDimList):
    for y, char in enumerate(layer):
      if char == '┌':
        boxIndexList.append([x, y, '┌'])
      elif char == '┐':
        boxIndexList.append([x, y, '┐'])
      elif char == '└':
        boxIndexList.append([x, y, '└'])
      elif char == '┘':
        boxIndexList.append([x, y, '┘'])
  return boxIndexList


def findBothLenghts(boxIndexList, direction):
  startAt = '┌'
  if direction == 'x':
    cordIndex = 0
    endAt = '┐'
  elif direction == 'y':
    cordIndex = 1
    endAt = '└'
  for corner in boxIndexList:
    if corner[2] != startAt:
      continue
    
    
    
  
  

mul = splitIntoMultidimList(garden)
print(findBox(mul))