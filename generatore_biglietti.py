"""*****************************************************
* Programma di generazione biglietti per la            *
* lotteria di SiVinceIlGnente.                         *
* Questo programma serve a generare un file            *
* contenente un numero finito di biglietti per         *
* la lotteria (giocate), con cui poi simulare          *
* le vincite.                                          *
* Autore: Francesco Tattoli aka Thuliast               *
* Data di creazione: 25-01-2023                        *
* Versione: 1.20                                       *
* PARAM EDITION: Questa versione accetta un parametro  *
* da riga di comando che decide se stampare a video il *
* progresso delle operazioni di scrittura o no. La     *
* stampa a video del progresso e' piu' lenta perche'   *
* deve aggiornare il video ad ogni passaggio, ed e'    *
* quindi consigliata per un numero limitato di         *
* biglietti, mentre la stampa "silent" e' consigliata  *
* in caso di generazione massiva di biglietti          *
*****************************************************"""

import os
import random
import string
from datetime import datetime
import sys


def main():

    parametro = sys.argv[1]
    #Il numero di giocate che il programma simulera'
    giocate = int(input("Quante giocate vuoi simulare? "))
    if (giocate > 1000):
        if (parametro=="v") or (parametro=="-v"):
            print("La stampa a video puo' impiegare diverso tempo")
            scelta=input("Sei sicuro (S/N) ?")
            if (scelta=="S") or (scelta=="s"):
                genera_biglietti(giocate,parametro)
            else:
                sys.exit()
        else:
            genera_biglietti(giocate,parametro="s")


def genera_biglietti(giocate,parametro):
    #Apriamo in modalita' scrittura il file che conterra'
    #i biglietti giocati, completi di codice giocata e
    #6 numeri giocati
    f = open('giocate.txt', 'w+')

    #Per uso futuro. Registro in variabile il momento dell'inizio
    #della procedura
    tempo_inizio = datetime.now()
    
    for j in range(giocate):
        #Genero la riga vuota, un array che contiene il codice
        #giocata e i numeri giocati
        riga = []
        
        #Genero la stringa del codice giocata, che dovra'
        #essere lunga 32 caratteri, cosi' da garantirne il
        #piu' possibile la sua unicita'
        #(NOTA: Per ridurre la dimensione del file finale
        #il codice giocata e' stato impostato a 32 bit, ma lo
        #si puo' aumentare o diminuire a piacere a seconda
        #delle necessita', ma cio' influira' sulla grandezza
        #del file finale e il carico di lavoro sulla CPU.)
        cod_giocata = []
        cod_giocata.append(random_codice_giocata(32))
        

        #Adesso generiamo i 6 numeri da abbinare al codice
        #giocata. In questo modo il "biglietto" sara' completo
        #e potremo scriverlo nel file di testo
        #Array contenente i numeri estratti
        estrazione = []
        #Estraggo 999 volte un numero. Dovrebbe bastare
        #per estrarre 6 numeri unici
        for i in range(999):
            #Controllo se ho gia' riempito l'array con
            #i 6 numeri estratti
            if len(estrazione) == 6:
                #Esco dal loop. Non ho bisogno di altri
                #numeri
                break
            estratto = random.randint(1,90)
            #Se il numero e' gia' estratto lo salto
            if estratto in estrazione:
                continue
            else:
                estrazione.append(estratto)
                
        #Ad estrazione terminata, ordino l'array contenente
        #i numeri estratti
        estrazione.sort()

        #Aggrego i due array nell'array riga, cosi' posso poi
        #scrivere nel file
        riga = str(cod_giocata) + str(estrazione) + '\n'

        if (parametro == "v") or (parametro == "-v"):
            #L'utente ha scelto di stampare a video il progresso delle operazioni
            os.system('cls')
            print("Scrittura giocata {} di {}".format(j+1, giocate))
            f.write(str(riga))

        f.write(str(riga))                        
    #Chiudo il file
    f.close()

    #Per uso futuro. Registro in variabile il momento della fine
    #della procedura
    tempo_fine = datetime.now()
    tempo_impiegato = tempo_fine - tempo_inizio
    print("Elaborazione completata in {0} secondi".format(tempo_impiegato.seconds))
    

def random_codice_giocata(lung):
    #Algoritmo di generazione casuale di una lettera o cifra
    #utile per comporre il codice giocata
    letters = string.ascii_lowercase
    numbers = string.digits
    fullcode = letters + numbers
    return ''.join(random.choice(fullcode) for i in range(lung))



if __name__=="__main__":
    main()
