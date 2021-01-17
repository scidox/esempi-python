import os
print(os.getcwd())#mostra la directory corrente
os.mkdir("new_dir")#crea una nuova directory
os.chdir("new_dir")
os.getcwd()#cosi abbiamo cambiato la directory corrente

os.mkdir("newer_dir")
os.rmdir("newer_dir")#rimuove la directory, funziona solo se vuota

os.listdir("website")#restituisce il contenuto della directory

#vediamo quali sono file o directory
#import os
dir="website"
for name in os.listdir(dir):
    fullname=os.path.join(dir,name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
