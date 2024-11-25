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

def cleanStr(messStr):
  cleanStr = ''
  for index, letter in enumerate(messStr):
    if letter not in '┌┐└┘.\n':
      cleanStr += '.'
    else:
      cleanStr += letter
  return(cleanStr)

garden = cleanStr(garden)

def splitIntoMultidimList(notMessyString):
  MultidimList = []
  for line in notMessyString.split('\n'):
    MultidimList.append(list(line))
  return MultidimList


def findCorner(multiDimList):
  cornerIndexList = []
  for x,  layer in enumerate(multiDimList):
    for y, char in enumerate(layer):
      if char != '.':
        cornerIndexList.append([x,y,char])
  return cornerIndexList

def makeOverlapCountArray(multiDimList):
  overlapCountArray = []
  for line in multiDimList:
    newLine = []
    for char in line:
      newLine.append(0)
    overlapCountArray.append(newLine)
  return overlapCountArray

def findHorizontalCorner(cornerIndexList):
  pass

def findVerticalCorner(cornerIndexList):
  pass

def findOppositeCorner(cornerIndexList):
  pass

def findBoxFromCorners(cornerIndexList):
  boxList = []

  

def findSnakeArea(multiDimList):
  overlapCountArray = makeOverlapCountArray(multiDimList)
  cornerIndexList = findCorner(multiDimList)
  boxes = []
  




print(findCorner(splitIntoMultidimList(garden)))