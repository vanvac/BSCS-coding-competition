def convertCamelToSnake(camelStr) -> str:
  snakeStr = ''
  for char in camelStr:
    if char.isupper():
      snakeStr += '_' + char.lower()
    else:
      snakeStr += char
  return snakeStr


def convertSnakeToCamel(snakeStr) -> str:
  camelStr = ''
  nextCharUpper = False
  for char in snakeStr:
    if char == '_':
      nextCharUpper = True
      continue
    elif nextCharUpper:
      nextCharUpper = False
      char = char.upper()
      camelStr += char
      continue
    camelStr += char
  return camelStr


def checkIfCamel(var) -> bool:
  if var.find('_') == -1:
    return True
  return False


def changeCaseAndRev(Listov) -> list:
  result = []
  for var in Listov:
    if checkIfCamel(var):
      result.append(convertCamelToSnake(var))
    else:
      result.append(convertSnakeToCamel(var))
  result.reverse()
  return result


def splitCamelSnake(LisVars) -> tuple[list, list]:
  camel = []
  snake = []
  for varName in LisVars:
    if checkIfCamel(varName):
      camel.append(varName)
    else:
      snake.append(varName)
  return camel, snake


def battle(varA, varB) -> str | None:
  if len(varA) > len(varB):
    return varA
  elif len(varB) > len(varA):
    return varB
  else:
    return None


def battleVars(camelVar, snakeVar) -> list:
  result = []
  counter = 0
  while counter < len(camelVar) and counter < len(snakeVar):
    if battle(camelVar[counter], snakeVar[counter]) is not None:
      result.append(battle(camelVar[counter], snakeVar[counter]))
    counter += 1
  return result


def task1() -> str:
  # Task 1 - convert snake to camel
  string1 = 'there_was_a_man_and_he_had_eight_sons_apart_from_that_he_was_nothing_more_than_a_comma_on_the_page_of_history_its_sad_but_thats_all_you_can_say_about_some_people_but_the_eighth_son_grew_up_and_married_and_had_eight_sons_and_because_there_is_only_one_suitable_profession_for_the_eighth_son_of_an_eighth_son_he_became_a_wizard_and_he_became_wise_and_powerful_or_at_any_rate_powerful_and_wore_a_pointed_hat_and_there_it_would_have_ended_should_have_ended'
  return convertSnakeToCamel(string1)


def task2() -> str:
  # Task 2 - convert camel to snake
  string2 = 'inADistantAndSecondhandSetOfDimensionsInAnAstralPlaneThatWasNeverMeantToFlyTheCurlingStarmistsWaverAndPartSeeGreatAtuinTheTurtleComesSwimmingSlowlyThroughTheInterstellarGulfHydrogenFrostOnHisPonderousLimbsHisHugeAndAncientShellPockedWithMeteorCratersThroughSeasizedEyesThatAreCrustedWithRheumAndAsteroidDustHeStaresFixedlyAtTheDestination'
  return convertCamelToSnake(string2)


def task3(normalList) -> str:
  # Task 3 - normal battle
  while len(normalList) > 1:
    camel, snake = splitCamelSnake(normalList)
    normalList = battleVars(camel, snake)
  return normalList[0]


def task4(reverseList) -> str:
  # Task 4 - Reverse the list and convert the case
  while len(reverseList) > 1:
    camel, snake = splitCamelSnake(reverseList)
    reverseList = battleVars(camel, snake)
  return reverseList[0]


if __name__ == "__main__":
  # Task 3 & 4 - Battle of the variables lists
  listOfVariables = ['label_grown_chain', 'shown_dozen', 'minorFixed', 'rug_laugh_delay_was', 'been_thing',
                     'byeJugLease', 'scale_ahead', 'fair_sob', 'powerBabyFortyBeach', 'raiseBaseWaterWrote',
                     'table_bun_why', 'ateIllHence', 'pilotTexasSteamSob', 'issueTeachFat', 'hadHairThrowExact',
                     'afterSuiteRangeMount', 'vitalWroteTexasClass', 'fortyBusy', 'ape_bit', 'droveScopeUsualRefer',
                     'two_minor_lit_car', 'alter_peace', 'did_argue_hence_motor', 'train_table', 'chainCross']
  reversedListOfVariables = changeCaseAndRev(listOfVariables)

  with open('output.txt', 'w') as out:
    out.write(task1() + '\n\n')
    out.write(task2() + '\n\n')
    out.write(task3(listOfVariables) + '\n\n')
    out.write(task4(reversedListOfVariables) + '\n\n')
    out.write('Made by Vachan')
