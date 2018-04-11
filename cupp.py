from math import *
from random import *
import sys
from time import sleep
nbr_bonne_info=0
rajoute_cara=0
rajoute_upper=0
print("Afin de générer le dictionnaire de mots de passe, veuillez rentrer les informations personnelles suivantes. Si une saisi comprend plusieurs mots, collez les sans espaces:")
nom = input("Entrez le nom : ").lower()
if nom:
    nom= nom.split()[0]
    if nom=="roux":
        nbr_bonne_info=nbr_bonne_info+1
#print(floor(len(nom)/2))
prenom = input("Entrez le prenom : ").lower()
if prenom:
    prenom= prenom.split()[0]
    if prenom=="marius":
        nbr_bonne_info=nbr_bonne_info+1
naiss = input("Entrez la date de naissance JJMMAAAA : ").lower()

while len(naiss) not in (0, 8):
    naiss = input("Entrez la date de naissance JJMMAAAA (BON FORMAT!!) : ").lower()
if len(naiss)>7:
    naiss1=naiss[0]+naiss[1]
    naiss2=naiss[2]+naiss[3]
    naiss3=naiss[4]+naiss[5]+naiss[6]+naiss[7]
else:
    naiss1=0
    naiss2=0
    naiss3=0
if naiss == "21091978":
    nbr_bonne_info=nbr_bonne_info+1
pet = input("Entrez le nom de l'animal de compagnie : ").lower()
if pet:
    pet= pet.split()[0]
    if pet=="olympe":
        nbr_bonne_info=nbr_bonne_info+1
travail = input("Entrez le nom de l'entreprise : ").lower()
if travail:
    travail= travail.split()[0]
    if travail=="p-t4international":
        nbr_bonne_info=nbr_bonne_info+1
compagnon_nom= input("Entrez le nom du compagnon / de la compagne : ").lower()
if compagnon_nom:
    compagnon_nom= compagnon_nom.split()[0]
    if compagnon_nom =="perle":
        nbr_bonne_info=nbr_bonne_info+1
compagnon_prenom= input("Entrez le prenom du compagnon / de la compagne : ").lower()
if compagnon_prenom:
    compagnon_prenom= compagnon_prenom.split()[0]
    if compagnon_prenom =="sylvie":
        nbr_bonne_info=nbr_bonne_info+1
num= input("Voulez vous rajouter un nombre à la fin ? ex: numéro de département. Si non, laissez vide :")
if num:
    num=num.split()[0]
    if num =="31":
        nbr_bonne_info=nbr_bonne_info+1
cara= input("Voulez vous rajouter des caractères spéciaux ? O ou N :")
if cara:
    if cara[0]=='O':
        rajoute_cara=1
        nbr_bonne_info=nbr_bonne_info+1
    else:
        rajoute_cara=0
maj= input("Voulez vous rajouter une majuscule au début ? O ou N :")
if maj:
    if maj[0]=='O':
        rajoute_upper=1
        nbr_bonne_info=nbr_bonne_info+1
    else:
        rajoute_upper=0
#print(nbr_bonne_info)
liste=[nom,prenom,pet,travail,compagnon_nom,compagnon_prenom]
#print(liste)
#print(rajoute_cara)
#print(rajoute_upper)
#print(naiss1)
#print(naiss2)
#print(naiss3)
liste2=[]
liste3=[]
liste4=[]
liste5=[]
liste6=[]

for i in liste:
    if i:
        liste2.append(i[:ceil(len(nom)/2)])
        liste2.append(i[ceil(len(nom)/2):])
    
liste2.append(naiss1)
liste2.append(naiss2)    
liste2.append(naiss3)
#print("liste 2 :")        
#print(liste2)
for i in liste2:
    for n in liste2:
        liste3.append(i+n)
#print("liste 3 :")
#print(liste3)
if rajoute_upper:
    print("rofl")
    for z in liste3:
        if(len(z)>2):
            liste4.append(z[0].upper()+z[1:])
#print("liste 4 :")
#print(liste4)
if rajoute_cara:
    for f in liste4:
        liste5.append(f+"$")
if num:
    for j in liste5:
        liste6.append(j+num)

#print("liste 5 :")
#print(liste5)
#print("liste 6 :")
#print(liste6)

shuffle(liste6)
if (nbr_bonne_info>7):
    liste6.insert(6,"goodpassword")
fichier = open("dictionnaire_passwords.txt", "a")
for i in liste6[:15]:
    fichier.write(i+"\n")
fichier.close()
i=0
sys.stdout.write(str(i)+" % des calculs terminés")
sys.stdout.flush()
while(i<100):
    if i>100:
        i=100
    sys.stdout.write('\b\r'+str(i))
    sys.stdout.flush()
    i=i+7
    sleep(1)
print("\n")
print("SELECTION DES MEILLEURS MOTS DE PASSE TERMINEE")
sleep(5)






