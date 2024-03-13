class Translator:
    dictionary = {}
    def __init__(self):
        pass


    def printMenu(self):
        print("------------------------------")
        print("  Traslator Alien-Italian")
        print("------------------------------")
        print("  1. Aggiungi nuova parola")
        print("  2. Cerca una traduzione ")
        print("  3. Cerca con wildcard")
        print("  4. Exit")
        print("------------------------------")


    def loadDictionary(self, dict):

        f = open(dict, 'r')
        riga = f.readline()
        while (riga != ""):
            elements = riga.strip("\n").split(" ")
            if (not self.dictionary.keys().__contains__(elements[0])):
                self.dictionary [elements [0]] = []
            self.dictionary[elements[0]].append(elements[1])
            riga = f.readline()
        f.close()


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        list = entry[1]

        if self.dictionary.keys().__contains__(entry[0]):
            for element in list:
                self.dictionary[entry[0]].append(element)
        else:
            self.dictionary [entry [0]] = []
            for element in list:
                self.dictionary[entry[0]].append(element)



    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        translation = self.dictionary[query]
        return translation

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        fields = query.split("?")
        translations = []

        for key in self.dictionary.keys():
            if (key.__contains__(fields[0])) and (key.__contains__(fields[1])) :
                tupla_temp = (key, self.dictionary[key])
                translations.append(tupla_temp)

        return translations

