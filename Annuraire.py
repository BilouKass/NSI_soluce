# Définition des fonctions 
# Définition des fonctions 
import os
import csv

def ajouter_contact():
    question = ["Nom", "n° de téléphone", "Mail", "pseudo instagram", "code postal"]
    infos = {}
    for q in question:
        V = input(f"Quel est son {q} ?")
        infos[q] = V
    return infos

def afficher_contacts(liste):
    print("Liste des contacts : ")

    for contact in liste:
        print(contact['Nom'])

def afficher_un_contact(liste,numero):
    print(f"Affichage détaillé du contact n°{numero}")
    contact = liste[numero]
    for key, item in contact.items():
        print(f"{key} : {item}")

def supprimer_contact(liste,numero):
    del liste[numero]

def sauvegarder_contacts(nom_fichier,liste):
    """ #partie 2
    with open(f"{nom_fichier}.txt", 'w') as file:
        for contact in liste:
            file.write("----contact----:\n")
            for k,v in contact.items():
                file.write(f"{k}: {v}\n")
    """ 
    #partie 3
    headline = ""
    for k in liste[0].keys():
        headline += f"{k}," #creation de la 1er ligne
    headline = headline[:-1] #j'enleve la derniere virgule
    with open(f"{nom_fichier}.csv", 'w') as file:
        file.write(f"{headline}\n") #je marque la 1er ligne
        for contact in liste: #pour chaque contact creer
            V = "{},{},{},{},{}\n".format(contact['Nom'], contact['n° de téléphone'], contact['Mail'], contact['pseudo instagram'], contact['code postal']) #concatenation des infos d'un contact
            file.write(V)#ecriture dans le fichier
    """#partie 3Bis
    champ = []
    with open(f"{nom_fichier}.csv", 'w') as file: #ouverture du fichier
        for contact in liste:
            for k in contact.keys():
                champ.append(k)
            break
        file = csv.DictWriter(file, fieldnames=champ)
        file.writeheader()
        for contact in liste:
            file.writerow(contact)
    """     

def charger_contacts(nom_fichier):
     #partie 3
    def listing(txt:str):#fonction en + pour gerer une chaine de caractere et la transformer en list
        txt = txt.replace('\n', '') #remplace \n par rien 
        txt = txt.split(',') #cree une list
        return txt
    l = []
    
    if os.path.isfile(f"{nom_fichier}.csv"): #test si le fichier x existe
        with open(f"{nom_fichier}.csv", 'r') as file:
            head = str(file.readline()) #lecture de la 1er ligne
            head = listing(head)
            
            for line in file:#pour chaque ligne dans la fichier (contact)
                line = listing(line)
                dic = {}
                for a in range(len(head)):
                    dic[head[a]] = line[a]
                l.append(dic)
            print(l)
            print("contact ajouté")
            return l
            
    else:
        print("le fichier recherché n'existe pas")
    """
#partie 3 bis
    if os.path.isfile(f"{nom_fichier}.csv"):
        l = []
        with open(f"{nom_fichier}.csv", 'r') as file:
            content = csv.DictReader(file)
            for ligne in content:
                l.append(dict(ligne))
            return l
    else:
        print("le fichier recherché n'existe pas")
    """
# Programme principal
if __name__ == "__main__":
    liste = []
    reponse =""
    while reponse != "q":
        print("Entrez o pour ouvrir un fichier.")
        print("Entrez a pour ajouter un contact.")
        print("Entrez l pour lister les contacts.")
        print("Entrez d pour afficher le détail d'un contact.")
        print("Entrez s pour supprimer un contact.")
        print("Entrez w pour sauvegarder les contacts.")
        print("Entrez q pour quitter (une sauvegarde des contacts sera faite).")
        reponse = input(" Que voulez vous faire ? ")

        if reponse == "o":
            print("Vous allez charger le contenu d'un fichier.")
            print("Attention, ces données remplaceront vos données actuelles")
            print("Laissez le nom vide pour renoncer.")
            nom_fichier = input("Donnez le nom du fichier à ouvrir : ")
            liste = charger_contacts(nom_fichier)

        elif reponse == "a":
            contact = ajouter_contact()
            liste.append(contact)
            print("Contact ajouté")
        elif reponse == "l":
            afficher_contacts(liste)
        elif reponse =="d":
            numero = int(input("Donnez le numéro du contact à afficher : "))
            afficher_un_contact(liste,numero)
        elif reponse == "s":
            numero = int(input("Donnez le numéro du contact à supprimer : "))
            supprimer_contact(liste,numero)
        elif reponse == "q" or reponse=='w':
            nom_fichier=input("Donnez le nom du fichier de sauvegarde : ")
            sauvegarder_contacts(nom_fichier,liste)
            print("Fichier sauvegardé")
        else :
            print("Je n'ai pas compris ...")
