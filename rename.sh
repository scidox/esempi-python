#!/usr/bin/env bash
#rename extensione file
ext=HTM
echo $ext
new=html
echo $new
for file in *.$ext; do
    name=$(basename "$file" .$ext)
    #echo mv "$file" "$name.$new" #test before execute mv 
    mv "$file" "$name.$new"
done
