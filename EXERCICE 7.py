# Créé par t.hausmann, le 11/09/2023 en Python 3.7
list_data = ["clé1", "valuer", "clé2", "valeur"]

def list_to_dict(list_data):
  dict_data = {}
  for index in range(0, len(list_data), 2):
    key = list_data[index]
    value = list_data[index + 1]
    dict_data[key] = value

  print(dict_data)
  return dict_data

list_to_dict(list_data)