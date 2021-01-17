import csv
f= open("csv_file.txt")
csv_f = csv.reader(f) #legge il contenuto del csv_file
for row in csv_f:   #unpack per decomprimere i file del txt
    name,phone,role=row
    print("Name : {}, Phone: {}, Role:{}".format(name,phone,role))
f.close()


#memorizzare i dati da scrivere nell'elenco
hosts=[["workstation.local","192.168.1.1"],["webserver.cloud","192.168.1.51"]]
#vogliamo memorizzarli nel csv

with open('hosts.csv',"w") as hosts_csv:
     writer=csv.writer(hosts_csv)
     writer.writerows(hosts) #con il comando cat dalla shell possiamo vedere
                             #il risultato

#write e read csv con dizionari
#dictread trasforma una riga di dati in un file csv in un dizionario, quindi
#possiamo accedere ai dati utilizzando il nome della colonna invece
#della posizione

with open("software.csv") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"],row["users"]))
