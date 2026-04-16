import random

class Giocatore:
    def __init__ (self, nome, punteggio):
        self.nome = nome
        self.punteggio = punteggio

    def __repr__ (self):
        return f"{self.nome}"

    def __lt__(self, b):
        if self.punteggio > b.punteggio:
            return 1
        elif self.punteggio == b.punteggio:
            if self.nome.__lt__(b.nome) is True:
                return 1

class Domanda:
    def __init__ (self, testo, livello, risposte=[]):
        self.testo = testo
        self.livello = livello
        self.risposte = risposte

    def __repr__(self):
        return f"{self.testo}{self.livello}\n{self.risposte}\n\n"

file = open ('domande.txt', 'r', encoding='utf-8')
lista_righe = (file.readlines())
# Se il programma viene eseguito senza chiudere il file, stranamente non viene rilevato alcun errore
file.close()

contatore_righe = 0
lista_domande = []
while (contatore_righe+5) < len(lista_righe):
    lista_domande.append(Domanda(lista_righe[contatore_righe], int(lista_righe[contatore_righe+1][0 : -1]), [lista_righe[contatore_righe+2], lista_righe[contatore_righe+3], lista_righe[contatore_righe+4], lista_righe[contatore_righe+5]]))
    contatore_righe += 7

print("Benvenuto in Trivia Game! Le domande saranno poste in ordine crescente di difficoltà.")
print("Per giocare, occorre digitare il nome o il numero corrispondente alla risposta che si vuole dare.\n")

punteggio_corrente = 0
sottolista = []
risposta_corretta = True

# while risposta_corretta == True:
while risposta_corretta:
    for o in lista_domande:
        if o.livello == punteggio_corrente:
            sottolista.append(o)
    if len(sottolista) == 0:
        print (f"Complimenti, hai raggiunto il punteggio massimo, che è {punteggio_corrente}!")
        break
    else:
        print (f"Domanda numero {punteggio_corrente+1}:\n")
        domanda_corrente = sottolista[random.randrange(0, len(sottolista))]
        print (domanda_corrente.testo, end='')
        ordine_risposte = [0, 1, 2, 3]
        random.shuffle(ordine_risposte)
        counter = 0
        while counter < 4:
            if domanda_corrente.risposte[ordine_risposte[counter]][-1] == '\n':
                print (f"{counter+1}) {domanda_corrente.risposte[ordine_risposte[counter]]}", end='')
            else: print (f"{counter+1}) {domanda_corrente.risposte[ordine_risposte[counter]]}")
            counter += 1
        flag = 0
        while flag == 0:
            print ("Risposta: ", end = '')
            risposta_utente = input ()
            counter = 0
            for p in domanda_corrente.risposte:
                if risposta_utente==p[0 : -1]:
                    flag = 1
            while counter < 4:
                if risposta_utente==str(counter+1):
                    flag = 1
                    break
                counter += 1
            if flag == 0:
                print ("La risposta data non è tra quelle selezionabili; riprova.")

        if risposta_utente==domanda_corrente.risposte[0][0 : -1]:
            print ("\nBravo, risposta corretta!\n\n")
            sottolista.clear()
            punteggio_corrente += 1
        elif counter < 4:
            if ordine_risposte[counter] == 0:
                print("\nBravo, risposta corretta!\n\n")
                sottolista.clear()
                punteggio_corrente += 1
            else:
                print("Risposta sbagliata. FIne del gioco. Punteggio:", punteggio_corrente)
                risposta_corretta = False
        else:
            print ("Risposta sbagliata. FIne del gioco. Punteggio:", punteggio_corrente)
            risposta_corretta = False


print ("Inserisci il tuo nickname: ", end='')
new_giocatore = Giocatore (input(), punteggio_corrente)

file = open ('punti.txt', 'r', encoding='utf-8')
lista_righe = (file.readlines())
file.close()

lista_giocatori = []
counter = 0
while counter < len(lista_righe):
    if lista_righe[counter][-1] == '\n':
        giocatore_da_inserire = Giocatore (lista_righe[counter][0:-3], int(lista_righe[counter][-2]))
    else: giocatore_da_inserire = Giocatore (lista_righe[counter][0:-2], int(lista_righe[counter][-1]))
    lista_giocatori.append(giocatore_da_inserire)
    counter += 1
lista_giocatori.append(new_giocatore)

lista_giocatori.sort()


file = open ('punti.txt', 'w', encoding='utf-8')
counter = 0
while counter < len(lista_giocatori)-1:
    file.write(f"{lista_giocatori[counter].nome} {lista_giocatori[counter].punteggio}\n")
    counter += 1
file.write(f"{lista_giocatori[len(lista_giocatori)-1].nome} {lista_giocatori[len(lista_giocatori)-1].punteggio}")
file.close()

# Gli oggetti risposta_utente e counter possono essere lasciati dentro il ciclo while ed essere
# ugualmente visibili dal resto del codice (cosa che in Java non sarebbe possibile)