"""***********************************************
* Programma di estrazione numeri per la lotteria *
* SiVinceIlGnente.                               *
* Questo programma simula una estrazione di 6    *
* numeri casuali che serviranno poi a simulare   *
* la gestione di una lotteria, con estrazione    *
* dei biglietti vincenti                         *
* Autore: Francesco Tattoli aka Thuliast         *
* Data di creazione: 25-01-2023                  *
* Versione: 1.11                                 *
***********************************************"""

import random

def main():
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

    #Ad estrazione terminata metto in ordine i numeri
    #nell'array e stampo a video il risultato
    estrazione.sort()
    print("Estrazione avvenuta. I numeri estratti sono:")
    print(estrazione)

            

if __name__=="__main__":
    main()
