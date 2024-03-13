import translator as tr
import dictionary as di

t = tr.Translator()
d = di.Dictionary()
t.loadDictionary("dictionary.txt")
exit = False

while(exit == False):

    t.printMenu()

    txtIn = input("Scrivi il numero corrispondente alla funzione da te desiderata: ")

    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere? \n ")
        txtIn = input("")
        d.addWord(txtIn)
        print("Aggiunta!")

    elif int(txtIn) == 2:
        print("Ok, quale parola devo cercare? \n ")
        txtIn = input("")
        print(f"{d.translate(txtIn)}")

    elif int(txtIn) == 3:
        pass
    elif int(txtIn) == 4:
        exit = True
        break
