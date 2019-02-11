#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:42:28 2019

@author: stovenhe
"""

print('nom du fichier?')
nom=input()
a=str(nom)
fichier = open(a,'r')
lignes=fichier.readlines()
codeasm=[]
imm='0'

def dec2bin(d,nb):
    """Représentation d'un nombre entier en chaine binaire (nb: nombre de bits du mot)"""
    if d == 0:
        return "0".zfill(nb)
    if d<0:
        d += 1<<nb
    b=""
    while d != 0:
        d, r = divmod(d, 2)
        b = "01"[r] + b
    return b.zfill(nb)


for ligne in lignes:
    lignesplit=ligne.split(" ")
    if lignesplit[0]=='stop\n':
        ligne_code='00000000000000000000000000000000' 
        codeasm+=[ligne_code]
    elif lignesplit[0]=='\n':
        print('veuillez retrouver votre code assembleur dans "codeasm.txt"')
    else:

        if lignesplit[0]=='add':
            ligne_code='00001'
        elif lignesplit[0]=='sub':
            ligne_code='00010'
        elif lignesplit[0]=='mult':
            ligne_code='00011'
        elif lignesplit[0]=='div':
            ligne_code='00100'
        elif lignesplit[0]=='and':
            ligne_code='00101'
        elif lignesplit[0]=='or':
            ligne_code='00110'
        elif lignesplit[0]=='xor':
            ligne_code='00111'
        elif lignesplit[0]=='shl':
            ligne_code='01000'
        elif lignesplit[0]=='shr':
            ligne_code='01001'
        elif lignesplit[0]=='slt':
            ligne_code='01010'
        elif lignesplit[0]=='sle':
            ligne_code='01011'
        elif lignesplit[0]=='seq':
            ligne_code='01100'
        elif lignesplit[0]=='load':
            ligne_code='01101'
        elif lignesplit[0]=='store':
            ligne_code='01110'
        elif lignesplit[0]=='jmp':
            ligne_code='01111'
        elif lignesplit[0]=='braz':
            ligne_code='10000'
        elif lignesplit[0]=='branz':
            ligne_code='10001'
        elif lignesplit[0]=='scall':
            ligne_code='10010'
        else:
            print('not readable')        
        var=lignesplit[1].split(",")
        if len(var)==3:
            r1=str(dec2bin(int(var[0][1:]),5))      ##r1 reçoit l'indice du registre
            if 'r' in var[1]:
                o=str(dec2bin(int(var[1][1:]),16))
                imm='0'
            else:
                imm='1'
                o=str(dec2bin(int(var[1][0:]),16))
            if var[2][1:]=='\n':
                r2='00000'
            else:
                r2=str(dec2bin(int(var[2][1:]),5))
            ligne_code+=r1
            ligne_code+=imm
            ligne_code+=o
            ligne_code+=r2
        elif ligne_code=='01111':
            imm='0'
            o=str(dec2bin(int(var[0][1:]),21))
            r=str(dec2bin(int(var[1][0:]),5))
            ligne_code+=imm
            ligne_code+=o
            ligne_code+=r
        elif ligne_code=='10000' or ligne_code=='10001':
            r=str(dec2bin(int(var[0][1:]),5))
            a=str(dec2bin(int(var[1][0:-1]),22))
            ligne_code+=r
            ligne_code+=a
        codeasm+=[ligne_code]  ### Pour écriture héxa: [format(int(ligne_code,2),'08x')]

fichier.close()
    
newfile=open('codeasm.txt','w')
for i in codeasm:
    newfile.write(i+'\n')
newfile.close()
            
         
