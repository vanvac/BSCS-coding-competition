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


def findDiffAndCheckIfChange(sholdChange, notChange, shouldChangeI, notChangeI, compare):
  if notChange != compare[notChangeI]:
    return False, 0
  else:
    return True, abs(sholdChange - compare[shouldChangeI])+1
  

def findBothLenghts(boxIndexList):
  startAt = '┌'
  coordIndex = 0
  XYLenght = []
  while coordIndex < 2:
    if coordIndex == 0: 
      endAt = '┐' 
      shouldChangeIndex = 0
      notChangeIndex = 1
    else: 
      endAt = '└'
      shouldChangeIndex = 1
      notChangeIndex = 0
    randomFcvkingSRLatch = False
    for coord in boxIndexList:
      if coord[2] == startAt and not randomFcvkingSRLatch:
        shouldChange = coord[shouldChangeIndex]
        notChange = coord[notChangeIndex]
        randomFcvkingSRLatch = True
        
      if coord[2] == endAt and randomFcvkingSRLatch:
        isDiff, diff = findDiffAndCheckIfChange(shouldChange, notChange, shouldChangeIndex, notChangeIndex, coord)
        if isDiff:
          XYLenght.append(diff)
          break

    if coordIndex == 1:
      for starCor in boxIndexList:
        if starCor[2] == startAt:
          boxIndexList.remove(starCor)
          break
    coordIndex += 1
  return XYLenght, boxIndexList

def calcArea(XYLenght):
  return XYLenght[0] * XYLenght[1]


cornersList = findBox(splitIntoMultidimList(garden))
XYLenght = None
addArea = []
while XYLenght != []:
  XYLenght, cornersList = findBothLenghts(cornersList)
  try:
    addArea.append(calcArea(XYLenght))
  except:
    break

print(addArea)