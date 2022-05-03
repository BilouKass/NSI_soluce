
ip = input("Entrez l'ip: ")
masque_n = int(input("Entrez le masque: "))

masque = "1"*masque_n + "0"*(32-masque_n)

ip_l = ip.split(".")
a = []
for i in ip_l:
    b = bin(int(i))
    c = b.replace("0b", "")
    if len(c) <= 8:
        a.append("0"*(8-len(c)) + c) 

reseau = []
c = 0
for i in a:
    p = "0b"
    for l in i:
        if l == masque[c] and l == "1":
            p+= "1"
        else: 
            p += "0"
        c += 1
    reseau.append(p)

end = reseau.copy()
end = ''.join(end).replace("0b", "")
end = end[0:masque_n] + end[masque_n:32].replace("0","1")

base_ip = "adresse du réseau: "+ str(int(reseau[0], 2)) + "." + str(int(reseau[1], 2)) + "."+str(int(reseau[2], 2)) + "." + str(int(reseau[3], 2))
first_ip = "1 er adresse utilisable:" + str(int(reseau[0], 2)) + "." + str(int(reseau[1], 2)) + "."+str(int(reseau[2], 2)) + "." + str(int(reseau[3], 2) + 1)
last_ip = f"Dernière adresse utilisable: " + str(int(end[0:8], 2)) + "." + str(int(end[8:16], 2)) + "." + str(int(end[16:24], 2)) + "." + str(int(end[24:32], 2) - 1)
brodcast = "broadcast: "+ str(int(end[0:8], 2)) +"."+ str(int(end[8:16], 2)) + "."+ str(int(end[16:24], 2))+"."+str(int(end[24:32], 2))
free_ip = 32 - masque_n

print(base_ip)
print(brodcast)
print(first_ip)
print(last_ip)
print("nombre d'adresse: " + str(2**free_ip))
print("adresses disponibles: " + str(2**free_ip - 2))