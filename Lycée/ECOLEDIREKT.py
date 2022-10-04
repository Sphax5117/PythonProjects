# Créé par t.hausmann, le 04/10/2022 en Python 3.7
mes_notes = [19, 2, 11]

def calculer_moyenne(notes):
    '''Calcule la moyenne des notes et et l'affiche'''
    for i in range(len(notes)):
        assert notes[i] < 20, "/ ! \ Une note ne peux pas dépasser 20"
        assert notes[i] > 0, "/ ! \ Une note ne peux pas être négatif"
    moyenne = sum(notes)/ len(notes)
    print(f"La moyenne est {moyenne}")

def max_value(notes):
    max = 0
    for i in range(len(notes)):
        if notes[i] > max:
            max = notes[i]
    print(f"La note maximale de la liste est {max}")

def min_value(notes):
    min = 20
    for i in range(len(notes)):
        if notes[i] < min:
            min = notes[i]
    print(f"La note minimale de la liste est {min}")

def value_under_8(notes):
    under8 = []
    for i in range(len(notes)):
        if notes[i] < 8:
            under8.append(notes[i])
    percent = (len(under8) * 100) / len(notes)
    print(f"Le pourcentage de notes strictement inférieures à 8 est : {percent}")

def value_above_8_under_12(notes):
    notesComprises = []
    for i in range(len(notes)):
        if notes[i] <= 8 and notes[i] < 12:
            notesComprises.append(notes[i])
    percent = (len(notesComprises) * 100) / len(notes)
    print(f"Le pourcentage de notes inférieures ou égale à 8 et inférieure à 12 est : {percent}")

def value_above_12(notes):
    above12 = []
    for i in range(len(notes)):
        if notes[i] >= 12:
            above12.append(notes[i])
    percent = (len(above12) * 100) / len(notes)
    print(f"Le pourcentage de notes supérieur ou égal à 12 est : {percent}")



calculer_moyenne(mes_notes)
max_value(mes_notes)
min_value(mes_notes)
value_under_8(mes_notes)
value_above_8_under_12(mes_notes)
value_above_12(mes_notes)