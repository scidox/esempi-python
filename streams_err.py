#!/usr/bin/env python3

data=input("This wil come from STDIN: ")
print("Now we write to STDOUT: "+ data)
raise ValueError("Now we generate an error to STDERR")
