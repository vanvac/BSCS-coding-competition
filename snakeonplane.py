garden = ''''''

def splitIntoMultidimList(WeirdString):
  MultidimList = []
  for line in WeirdString.split('\n'):
    MultidimList.append(list(line))
  return MultidimList


def findBox(multiDimList):
  boxIndexList = []
  for y,  layer in enumerate(multiDimList):
    for x, char in enumerate(layer):
      if char == '┌':
        boxIndexList.append([x, y, '┌'])
      elif char == '┐':
        boxIndexList.append([x, y, '┐'])
      elif char == '└':
        boxIndexList.append([x, y, '└'])
      elif char == '┘':
        boxIndexList.append([x, y, '┘'])
  return boxIndexList

