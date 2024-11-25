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

def findSnakeArea(multiDimList):
  pass

print(findBox(splitIntoMultidimList(garden)))