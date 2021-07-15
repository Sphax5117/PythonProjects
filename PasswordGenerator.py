import random
import string


method_chose = input("What method do you want ? \n For just lowercase letter, type 1 \n For lower AND uppercases, type 2 \n  For lower, upper and digits, type 3 \n For lower, upper, digits and punctuation, type 4 : ")
nbc = input("How many character do you want ? ")

if method_chose == "1":
    mdp = ''.join(random.choices( string.ascii_lowercase, k=int(nbc)))
    print("Your random password is " + str(mdp))
elif method_chose == "2":
    mdp = ''.join(random.choices( string.ascii_lowercase + string.ascii_uppercase, k=int(nbc)))
    print("Your random password is " + str(mdp))
elif method_chose == "3":
    mdp = ''.join(random.choices( string.ascii_lowercase + string.ascii_uppercase + string.digits , k=int(nbc)))
    print("Your random password is " + str(mdp))
elif method_chose == "4":
    mdp = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=int(nbc)))
    print("Your random password is " + str(mdp))
else:
    print("You choose a choice wich do not exist !")
