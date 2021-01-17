import os #per prendere le informazioni dal sistema operativo
os.remove("novel.txt")#rimuove il file novel.txt
os.rename("first_draft.txt","finished.txt")#rinomina il file
os.path.exists("finished.txt")#ci dice se il file esiste con True o False

os.path.getsize("speed.txt")#ci dice la grandezza del file
os.path.getmtime("speed.txt")#tempo in formato unix usato spesso

import datetime
timestamp=os.path.getmtime("speed.txt")
datetime.datetime.fromtimestamp(timestamp)#data molto + facile da leggere

os.path.abspath("speed.txt")#ci dice il percorso assoluto del file
