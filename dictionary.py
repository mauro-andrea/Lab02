import translator as t
t = t.Translator()

class Dictionary:
    def __init__(self):
        self.dictionary = {}

    def addWord(self, userIn):
        fields = userIn.lower().split(" ")
        l = []
        for i in range (len(fields)):
            if (i != 0) and (fields[i] != "") :
                l.append(fields[i])
        tupla = (fields[0], l)
        t.handleAdd(tupla)

    def translate(self, userIn):
        word = userIn.lower().strip(" ")
        translation = t.handleTranslate(word)
        return translation
    def translateWordWildCard(self, userIn):
        word = userIn.lower().strip(" ")
        translations = t.handleWildCard(word)
        return translations

