#!/usr/bin/env python3

import random
import webbrowser

name= input ("Please enter your name: ")
print("Ciao, "+ name)

name= input ("Cosa vuoi cercare su Bing? ")
#cicli=int(input ("quante volte:"))
webbrowser.get("firefox").open('https://www.bing.com/search?q='+str(name))

#for n in range(cicli):
    #value=random.randint(0,2560)
    #webbrowser.open('https://www.bing.com/search?q=test'+str(name)+ str(value))
    #webbrowser.open('https://www.bing.com/search?q=gio'+str(name)+ str(value))
