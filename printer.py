import tempfile
import win32api
import win32print
import os


filename ="felipe.txt"
SS=0.01

for i in range (0,168):
    SS=SS*2

SM=0.01

for i in range (0,182):   
   SM=SM*2
   
    
print("SS = " + str(SS)+ "\nSM = "+str(SM))
open(filename, "w").write("Salarion en 24 semanas = "+ str(SS) +"\n Salario en 6 meses (182)= "+ str(SM))
win32api.ShellExecute(0,"print",filename, None ,".",0)
