def calcul(expression):
  pile = [] ##Initialisation de la piles

  for token in expression:
    if token in "+-*/":
      op2 = pile.pop()
      op1 = pile.pop()
      result = eval(f"{op1}{token}{op2}")
      pile.append(result)
    else:
      pile.append(int(token)) ## on ajoute le nombre a la pile
  return pile.pop()

expression = "456++3*"
print(calcul(expression))

