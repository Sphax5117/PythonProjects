def is_goodpar(expression):

  pile = []
  for char in expression:
    if char in ("(", "["):
      pile.append(char)
    elif char in (")", "]"):
      if len(pile) == 0:
        return False
      else:
        top = pile.pop()
        if char == "]" and top == "(":
          return False
  return len(pile) == 0

expression = "[3 + (5 - 7)] * 3"
print(is_goodpar(expression))