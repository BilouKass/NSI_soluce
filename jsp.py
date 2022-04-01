#CHANGEZ LE NOM DES VARIABLES !!!

def triSelection(l): #tri selection comme on à fait en cour (on l'a recopier dans le cahier)
    """ 
    triSelection prend en entrée une liste l
    en sortie, on a la liste l2 triée grâce au tri sélection
    On effectue ce tri en positionnant les plus petits à gauche
    """

    for i in range(len(l)):
        # Trouver le min
        min = i
        for x in range(i +1, len(l)):
            if l[min] > l[x]:
                min = x
                    
        temp = l[i]
        l[i] = l[min]
        l[min] = temp
    return l

def demander_notes():
    notes = {}
    nb_notes = int(input("Combien de notes voulez vous rentrer ?"))
    for _ in range(nb_notes):
        nom = input("Nom de l'élève: ")
        note = float(input("note: "))
        notes[nom] = note
    return notes
    
def affiche_eleves_classes(dic):
    """
    En entrée : un dictionnaire dont les clefs/valeurs sont les noms 
    des élèves et les notes
    Pas de sortie (aucun return)
    La fonction utilise print pour afficher les élèves par ordre des notes,
    du plus petit au plus grand
    
    """
    # Mettez votre code ici
    while len(dic) != 0: #s'execute tant que le dictionnaire contient quelque chose
        for k, v in dic.items(): #trouve le 1er élément du dico (on à pas la clé)
            maxi = v
            m_name = k
            break #arrêt de la boucle

        for k,v in dic.items(): #recherche du max
            if v > maxi:
                maxi = v
                m_name = k
        print(f"{m_name} as eu {maxi}")
        del dic[m_name] #suppression du plus haut élément en note

if __name__ == "__main__":
    # Test du tri selction
    assert triSelection([3,7,5,8,1])==[1,3,5,7,8], "mauvais tri selection"
    # programme principal
    d = demander_notes()
    print(d)
    affiche_eleves_classes(d)