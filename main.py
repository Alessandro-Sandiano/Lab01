import operator
import random


class Domanda:
    def __init__(self, testo="", livello="", corretta="", risposte=[]):
        self.testo = testo
        self.livello = livello
        self.corretta = corretta
        self.risposte = risposte

listaDomande = []
with open("domande.txt", encoding="utf-8") as file:
    while True:
        listaDomande.append(Domanda(file.readline().strip(), file.readline().strip(), file.readline().strip(), [file.readline().strip(), file.readline().strip(), file.readline().strip()]))
        if file.readline()=="": break

print("Benvenuto a Trivia Game! Digitare la risposta corretta o il numero ad essa corrispondente.\n")
punteggio = 0
corretta = True

while corretta is True:

    listaDomandePerLivello = [l for l in listaDomande if int(l.livello)==punteggio]
    if len(listaDomandePerLivello) == 0: break

    domandaEstratta = listaDomandePerLivello[random.randint(0, len(listaDomandePerLivello)-1)]
    domandaEstratta.risposte.append(domandaEstratta.corretta)
    random.shuffle(domandaEstratta.risposte)

    print("\nLivello " + str(punteggio) + ") " + domandaEstratta.testo)
    for r in domandaEstratta.risposte:
        print(f"{domandaEstratta.risposte.index(r) + 1}. {r}")
    print("\nInserisci la risposta: ", end="")

    while True:
        risposta = input()
        if risposta == "":
            print("Non è stata inserita alcuna risposta. Riprovare: ", end="")
            continue
        try:
            if int(risposta) in range(1, len(domandaEstratta.risposte)+1):
                if domandaEstratta.risposte[int(risposta)-1] == domandaEstratta.corretta:
                    print("Risposta corretta!")
                    punteggio+=1
                else:
                    print(f"Risposta sbagliata! La risposta corretta era: {domandaEstratta.risposte.index(domandaEstratta.corretta)+1}")
                    corretta = False
                break
            print("Il numero inserito non è associato ad alcuna risposta. Riprovare: ", end="")
        except:
            if risposta in domandaEstratta.risposte:
                if risposta==domandaEstratta.corretta:
                    print("Risposta corretta!")
                    punteggio+=1
                else:
                    print(f"Risposta sbagliata! La risposta corretta era: {domandaEstratta.risposte.index(domandaEstratta.corretta)+1}")
                    corretta = False
                break
            print("La risposta non è stata digitata correttamente. Riprovare: ", end="")

print("\nHai totalizzato " + str(punteggio) + " punti!")
nomeUtente = input("Inserisci il tuo nickname: ")

punteggi = [f"{nomeUtente} {punteggio}\n"]
with open("punti.txt", encoding="utf-8") as file:
    '''
    while True:
        punteggi.append(file.readline())
        if punteggi[len(punteggi)-1]=="":
            punteggi.pop(len(punteggi)-1)
            break
    '''
    punteggi.extend(file.readlines())

'''
punteggi.sort(key=operator.itemgetter(0))
punteggi.sort(key=operator.itemgetter(-2), reverse=True)
'''
punteggi.sort(key=lambda p: (-ord(p[-2]), p[0]))

with open("punti.txt", "w", encoding="utf-8") as file:
    for p in punteggi:
        file.write(p)