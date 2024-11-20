function SnakeCaseToCamel(snakeStr)
  local camelStr = ""
  local isNextUp = false
  for letter in snakeStr do
    if isNextUp then
      camelStr = camelStr .. string.upper(letter)
    elseif letter == '_' then
      isNextUp = true
    else
      camelStr = camelStr .. letter
    end
  end
end

local message = "Hello World"
print(SnakeCaseToCamel("snake_case_to_camel_case"))