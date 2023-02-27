# PyLottery
Un esempio di gestione Lotteria. Con generazione biglietto, generazione massiva biglietti e verificatore di vincite

Versione funzionante del programma di Gestione Lotteria.
Il pacchetto comprende 3 files
- estrazione_numeri.py - E' l'algoritmo principale, cioe' quello che ho usato per generare una lista di 6 numeri casuali, compresi tra 1 e 90, che viene usato come esempio nel file successivo, "generatore_biglietti.py"
- generatore_biglietti.py - Questo programma permetta all'utente di "simulare" un numero di biglietti (le giocate) e di assegnare ad ogni biglietto un codice giocata, composto da una chiave unica a 32 caratteri, e 6 numeri casuali, compresi tra 1 e 90, scrivendo il tutto in un file di testo (giocate.txt). Il numero di biglietti da simulare e' richiesto all'utente
- verifica_vincite.py - Il programma che si occupa di verificare il file di testo "giocate.txt" alla ricerca dei biglietti vincenti. Viene richiesto all'utente di inserire i 6 numeri vincenti (l'estrazione), e la procedura verifichera', riga per riga, se il biglietto e' vincente, e quanti numeri vincenti sono stati estratti. Il programma registra in un apposito file di testo (vincite.txt) le vincite registrate, e stampa a video le statistiche sui biglietti vincenti (quanti biglietti sono vincenti, quanti hanno fatto 2 punti, quanti hanno fatto 3, e cosi' via)
