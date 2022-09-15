# Créé par t.hausmann, le 15/09/2022 en Python 3.7

from datetime import timedelta

sec = int(input("secondes"))
formatSecondes = timedelta(seconds=sec)
print(str(formatSecondes))
