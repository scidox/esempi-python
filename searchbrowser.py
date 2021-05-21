#!/usr/bin/env python3

import webbrowser

name= input ("What content of the text file do you want to search on web? ")
file=open(name)

cicli=int(input ("how many lines do you want to search for:"))

for n in range(cicli):
        lettura=file.readline()
        print(lettura)
        webbrowser.open('https://www.bing.com/search?q='+str(lettura))
        #firefox
        #webbrowser.get("firefox").open('https://www.bing.com/search?q='+str(lettura))
