## Created by Hausmann Tom on 21/11/2022
## coding __utf8__
import random


infinitive = ["bear","beat","become","begin","bend","bet","bid","bid","bite","bleed","blow","break","breed","bring","build","burn","burst","buy","cast","catch","choose","cling","come","cost","creep","cut","deal","dig","dive","do","draw","dream","drink","drive","eat","fall","feed","feel","fight","find","flee","fling","fly","forbid","forget","forgive","freeze","get","give","go","grind","hang","hear","hide","hit","hold","hurt","keep","kneel","know","lay","lead","lean","leap","learn","leave","lend","let","lie","light","lose","make","mean","mow","pay","put","quit","read","ride","ring","rise","run","saw","say","see","seek","sell","send","set","sew","shake","shed","shine","shoot","show","shrink","shut","sing","sink","sit","sleep","slide","smell","sow","speak","speed","spell","spend","spill","spin","spit","split","spoil","spread","spring","stand","steal","stick","stink","stride","strike","string","swear","sweep","swell","swim","swing","take","teach","tear","tell","think","throw","tread","understand","undertake","upset","wake","wear","weave","weep","wind","win","withdraw","wring","write"]
preterit = ["bore","beat","became","began","bent","bet / betted (US)","bid","bade / bid (US)","bit","bled","blew","broke","bred","brought","built","burnt / burned","burst","bought","cast","caught","chose","clung","came","cost","crept","cut","dealt","dug","dove","did","drew","dreamt / dreamed","drank","drove","ate","fell","fed","felt","fought","found","fled","flung","flew","forbad/forbade (US)","forgot","forgave","froze","got","gave","went","ground","hung / hanged","heard","hid","hit","held","hurt","kept","knelt / kneeled (US)","knew","laid","led","leant / leaned","leapt","learnt / learned","left","lent","let","lay","lit / lighted","lost","made","meant","mowed","paid","put","quit / quitted","read","rode","rang","rose","ran","sawed","said","saw","sought","sold","sent","set","sewed","shook","shed","shone","shot","showed","shrank /shrunk (US)","shut","sang","sank","sat","slept","slid","smelt / smelled","sowed","spoke","sped / speeded","spelt / spelled","spent","spilt / spilled","span / spun","spat / spit","split","spoilt / spoiled","spread","sprang / sprung","stood","stole","stuck","stank / stunk","strode","struck","strung","swore","swept","swelled","swam","swung","took","taught","tore","told","thought","threw","trod","understood","undertook","upset","woke / waked","wore","wove / weaved","wept","wound","won","withdrew","wrung","wrote"]
participe = ["borne","beaten","become","begun","bent","bet / betted (US)","bid","bid / bidden","bitten","bled","blown","broken","bred","brought","built","burnt / burned","burst","bought","cast","caught","chosen","clung","come","cost","crept","cut","dealt","dug","dived","done","drawn","dreamt / dreamed","drunk","driven","eaten","fallen","fed","felt","fought","found","fled","flung","flown","forbidden","forgotten","forgiven","frozen","got/gotten (US)","given","gone","ground","hung / hanged","heard","hid(den)","hit","held","hurt","kept","knelt / kneeled (US)","known","laid","led","leant / leaned","leapt","learnt / learned","left","lent","let","lain","lit / lighted","lost","made","meant","mown / mowed (US)","paid","put","quit / quitted","read","ridden","rung","risen","run","sawn","said","seen","sought","sold","sent","set","sewn","shaken","shed","shone","shot","shown","shrunk","shut","sung","sunk","sat","slept","slid","smelt / smelled","sown","spoken","sped / speeded","spelt / spelled","spent","spilt / spilled","spun","spat / spit","split","spoilt / spoiled","spread","sprung","stood","stolen","stuck","stunk","strid(den)","struck","strung","sworn","swept","swollen / swelled","swum","swung","taken","taught","torn","told","thought","thrown","trod(den)","understood","undertaken","upset","woken / waked","worn","woven / weaved","wept","wound","won","withdrawn","wrung","written"]
trad = ["supporter","battre","devenir","commencer","courber","parier","faire une enchère","ordonner","mordre","saigner","souffler","casser","élever","apporter","construire","brûler","éclater","acheter","lancer","attraper","choisir","s'accrocher","venir","coûter","ramper","couper","distribuer","creuser","plonger","faire","dessiner","rêver","boire","conduire","manger","tomber","nourrir","se sentir","combattre","trouver","fuir","lancer","voler (mouvement)","interdire","oublier","pardonner","geler","obtenir","donner","aller","moudre","pendre","entendre","cacher","frapper","tenir","blesser","garder","s'agenouiller","connaître","poser (à plat)","mener","pencher","bondir","apprendre","quitter","prêter","laisser","être allongé","éclairer","perdre","faire","signifier","tondre","payer","mettre","arrêter","lire","chevaucher","sonner","s'élever","courir","scier","dire","voir","chercher","vendre","envoyer","placer","coudre","secouer","verser","briller","tirer (arme)","monter","rétrécir","fermer","chanter","couler (bateau)","être assis","dormir","glisser","sentir","semer","parler","aller vite","épeler","dépenser","renverser","faire tourner","cracher","fendre","gâcher","répandre","bondir","être debout","voler (qqch)","coller","puer","marcher à grands pas","frapper","enfiler","jurer","balayer","se gonfler","nager","se balancer","prendre","enseigner","déchirer","dire","penser","lancer","fouler","comprendre","entreprendre","bouleverser","réveiller","porter (vêtement)","tisser","sangloter","enrouler","gagner","retirer","tordre","écrire",""]
playAgain = True

total = 0
points = 0

def frenchMode():
    global total
    global points
    wordPos = random.randint(0,len(trad) - 1)
    word = trad[wordPos]
    associatedWords = [infinitive[wordPos], preterit[wordPos], participe[wordPos]]
    tense = ""
    print(word)
    for i in range(3):
        if i == 0:
            tense = "infinitive"
        elif i == 1:
            tense = "preterit"
        elif i == 2:
            tense = "participe"
        inputWord = input(f" {tense} : ")
        if inputWord == associatedWords[i]:
            print(f"you're right {inputWord} is the {tense} of '{word}' \n")
            points += 1
            total += 1
            print(f"You have now {points} points out of {total}")
        else:
            print(f"WRONG ! The {tense} of {word} is '{associatedWords[i]}'\n")
            total += 1
            print(f"You have now {points} points out of {total}")


while playAgain == True:
    frenchMode()

