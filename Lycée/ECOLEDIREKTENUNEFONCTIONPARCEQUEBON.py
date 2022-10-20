# Créé par t.hausmann, le 20/10/2022 en Python 3.7
# -*- coding UTF-8 -*-
# Ecole directe
mes_notes = [13, 16, 5, 12, 16, 20, 12, 8, 17, 17, 7, 18, 5, 16, 7, 8, 15, 13, 11, 10, 15, 14, 17, 13, 19, 6, 14, 8, 16, 8, 10, 11, 19, 7, 5]

def ecoleDirekt(notes):

    moyenne = round(sum(notes)/ len(notes), 2)
    max = 0
    min = 20
    under8 = []
    notesComprises = []
    above12 = []
    for i in range(len(notes)):
        if notes[i] > max:
            max = notes[i]
        if notes[i] < min:
            min = notes[i]
        if notes[i] < 8:
            under8.append(notes[i])
        if notes[i] <= 8 and notes[i] < 12:
            notesComprises.append(notes[i])
        if notes[i] >= 12:
            above12.append(notes[i])

    percentUnder8 = round((len(under8) * 100) / len(notes),2)
    percent8_12 = round((len(notesComprises) * 100) / len(notes))
    percentAbove12 = round((len(above12) * 100) / len(notes))

    finalValues = (moyenne, max, min, percentUnder8, percent8_12, percentAbove12)
    print(finalValues)
    return finalValues

assert ecoleDirekt(mes_notes) == (12.23, 20, 5, 20, 31, 57), "/!\ ecoleDirekt"



