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
    """
    with open(f"{nom_fichier}.txt", 'w') as file:
        for contact in liste:
            file.write("----contact----:\n")
            for k,v in contact.items():
                file.write(f"{k}: {v}\n")
    """
    headline = ""
    for k in liste[0].keys():
        headline += f"{k},"
    headline = headline[:-1]
    with open(f"{nom_fichier}.csv", 'w') as file:
        file.write(f"{headline}\n")
        for contact in liste:
            V = "{},{},{},{},{}\n".format(contact['Nom'], contact['n° de téléphone'], contact['Mail'], contact['pseudo instagram'], contact['code postal'])
            file.write(V)
    """
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
    """
    def listing(txt:str):
        txt = txt.replace('\n', '')rint("Contact ajouté")
    l = []
    
    if os.path.isfile(f"{nom_fichier}.csv"):
        with open(f"{nom_fichier}.csv", 'r') as file:
            head = str(file.readline())
            head = listing(head)
            
            for line in file:
                line = listing(line)
                dic = {}
                for a in range(len(head)):
                    dic[head[a]] = line[a]
                l.append(dic)
            print(l)
            return l
    else:
        print("le fichier recherché n'existe pas")
    """

    if os.path.isfile(f"{nom_fichier}.csv"):
        l = []
        with open(f"{nom_fichier}.csv", 'r') as file:
            content = csv.DictReader(file)
            for ligne in content:
                l.append(dict(ligne))
            return l
    else:
        print("le fichier recherché n'existe pas")

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