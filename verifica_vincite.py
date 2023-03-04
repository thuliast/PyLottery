"""*****************************************************
* Programma di lettura biglietti per la lotteria di    *
* SiVinceIlGnente.                                     *
* Questo programma serve a controllare un file         *
* contenente un numero finito di biglietti per         *
* la lotteria (giocate), mettendolo a confronto con    *
* una estrazione, e scrive in un altro file le vincite.*
* Autore: Francesco Tattoli aka Thuliast               *
* Data di creazione: 25-01-2023                        *
* Versione: 1.5                                        *
*****************************************************"""
import os

def main():
    #Array contenente l'estrazione
    estrazione = []
    #Array contenente il codice giocata. Se non lo dichiaro come
    #array me lo tiene come stringa, e nel file delle vincite non
    #viene scritto bene
    codice_giocata = []
    #Contatori delle vincite. Il primo conteggia le vincite totali
    #e poi ci sono i contatori per le singole vincite pagabili
    tot_conta_vincite = 0
    conta_vincite_2 = 0
    conta_vincite_3 = 0
    conta_vincite_4 = 0
    conta_vincite_5 = 0
    conta_vincite_6 = 0
    #Array contenente i numeri giocati. Serve crearlo come array
    #per confrontare ogni singolo elemento con l'array dell'estrazione
    num_giocati = []
    terminato = False
    i = 1

    #Richiedo all'utente di digitare i 6 numeri estratti
    #for i in range(1,7):
    while not terminato:
        if i > 6:
            terminato == True
            break
        estratto = input("Digita il %d° numero estratto:" % i)

        if estratto.isdigit():
            if (estratto < '1') or (estratto > '90'):
                print("Numero non corretto")
                continue
            estrazione.append(str(estratto))
            i += 1
        else:
            print("Numero non corretto")
            continue

        
            
        

        #Per il momento evito di complicare il programma inserendo
        #controlli se il numero e' positivo, e' compreso tra 1 e 90
        #o se non e' stato gia' estratto. Mi affido alla buona
        #fede dell'operatore che digita i numeri
        #estrazione.append(str(estratto))

    #Stampo un messaggio di cortesia di attesa mentre viene effettuata
    #la verifica sul file delle giocata
    os.system('cls')
    print("Attendere. Verifica vincite in corso...")

    #Metto in ordine i numeri nell'array
    estrazione.sort()

    #Apro il file contenente le giocate, e calcolo la lunghezza
    #cosi' so quanto lungo deve essere il ciclo di lettura delle
    #giocate
    f = open('giocate.txt','r')
    lung = f.readlines()
    num_linee = len(lung)
    
    #Chiudo e riapro il file per evitare problemi di EOF o letture strane
    f.close()
    f = open('giocate.txt','r')
    
    #Prima di far partire il loop apro anche il file in cui finiranno
    #le giocate vincenti. 
    j = open('vincite.txt','w+')

    #Parto col loop che verifica le vincite. Buona fortuna :-)
    for i in range(num_linee):
        
        riga = f.readline()
        #OK. La riga e' una stringa unica, compreso di apici e
        #parentesi perche' le operazioni sui file tramutano tutto
        #in stringa, quindi devo 'artigianalmente' estrarre
        #la parte relativa al codice giocata e i 6 numeri
        num_giocati_raw = riga[37:-2]
        num_giocati_raw2 = list(num_giocati_raw.split(','))
        for element in num_giocati_raw2:
            o = element.replace(' ','')
            num_giocati.append(o)
        #Completata la pulizia dai caratteri sporchi del file di
        #input passo a verificare le vincite confrontando i due
        #array e, tramite la funzione set, scopro le uguaglianze
        #nelle righe
        vittorie = set(num_giocati) & set(estrazione)
        if len(vittorie) >= 2:
            codice_giocata.append(riga[2:34])
            #riga = str(codice_giocata) + str(num_giocati) + '\n'
            riga = str(codice_giocata) + str(list(vittorie)) + '\n'
            j.write(str(riga))

            tot_conta_vincite += 1
            if len(vittorie) == 2:
                conta_vincite_2 += 1
            if len(vittorie) == 3:
                conta_vincite_3 += 1
            if len(vittorie) == 4:
                conta_vincite_4 += 1
            if len(vittorie) == 5:
                conta_vincite_5 += 1
            if len(vittorie) == 6:
                conta_vincite_6 += 1

        #Svuoto gli array num_giocati e codice_giocata
        # prima di passare al ciclo successivo
        num_giocati.clear()
        codice_giocata.clear()

        


    #Prima di terminare la procedura chiudo i file
    f.close()
    j.close()
    print("****************************************************************") 
    print("* Controllo Terminato. Totale Vincite registrate:" , tot_conta_vincite, " *")
    print("Vincite da 2 numeri: ", conta_vincite_2, " *")
    print("Vincite da 3 numeri: ", conta_vincite_3, " *")
    print("Vincite da 4 numeri: ", conta_vincite_4, " *")
    print("Vincite da 5 numeri: ", conta_vincite_5, " *")
    print("Vincite da 6 numeri: ", conta_vincite_6, " *")
    print("****************************************************************") 


if __name__=="__main__":
    main()
