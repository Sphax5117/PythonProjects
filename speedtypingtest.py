import keyboard

f = open("1-1000.txt", "r")


while True:
    a = f.readline()
    for letter in a:
        print(a)
        print(keyboard.read_key())
        if keyboard.read_key() == letter:
            print("VAMOOSSS")
        else:
            print("Wrong key")

    
