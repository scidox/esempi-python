file = open ("spider.txt")
print(file.readline()) #stampa il contenuto del file, solo la prima riga e
#aggiorna la posizione corrente nel
#file richiamarlo una seconda volta produce la riga successiva
print(file.read()) #stampa il contenuto del file, in questo caso parte dalla
#seconda riga fino alla fine del file
file.close() #chiudo il file



with open("spider.txt") as file:
    print(file.readline())
    #in questo caso con il blocco with c'è la chiusura automatica del file


with open("spider.txt") as file:
     for line in file:
         print(line.upper()) #legge il file e lo visualizza tutto in maiuscolo
                             #ma con righe bianche vuote tra un teso e un altro

with open("spider.txt") as file:
     for line in file:
         print(line.strip().upper())#tolgo le linee vuote


file=open("spider.txt")
lines=file.readlines()
file.close() #anche se ho chiuso il file il lines è rimasto memorizzato
lines.sort()
print(lines)#vengono visualizzate le righe del file in ordine alfabetico,
            #e presentano \n alla fine di ogni riga per dire che c'è una nuova
            #linea dopo

with open("novel.txt","w" ) as file: #"w" apre il file in scrittura e cancella
                                     #quello che c'è scritto, utilizzare "a" per 
                                     #aggiungere righe
     file.write("Era una notte buia e tempestosa, quando i cyborg")

      #in caso di successo scrive il numero di caratteri aggiunti al file
