import random
class Domanda(object):
    def __init__(self, testo="", diff=None, corretta="", opzioni=[]):
        self.testo=testo
        self.difficoltà=diff
        self.corretta=corretta
        self.opzioni=opzioni


    def opzioni_random(self):
        random.shuffle(self.opzioni)
        return self.opzioni