# Saisir une liste de nombres séparés par des virgules
nombre = input("Saisir une liste de nombres séparés par des virgules")

# Séparer l'ensemble des nombres et les insérer dans une liste
liste = nombres.split(",")

# Affichage
print("Liste des nombre: ", liste )

# Liste est une chaîne de caractère
# Convertir les elements de la liste en enier
liste_entiers = []
for nombre in liste:
  nombre_entier = int(nombre)
  liste_entiers.append(nombre_entier)

# calculez la somme des entiers
somme = 0
for nombre in liste_entiers:
  somme += nombre 

# Equivalent à:
# somme
print("Somme des nombres:", somme)

# effectuez la moyenne
moyenne = somme / len(liste_entiers)
print("moyenne des nombres:", moyenne)

# Trouvez combien de nombre de la liste sont superieurs à la moyenne
nombre_au_dessus_moyenne = 
for nombre in liste_entiers:
  if nombre > moyenne:
    nombre_au_dessus_moyenne += 
print("Nombre de nombres superieurs à la moyenne:", nombre_au_dessus_moyenne)

# Nombre
nombres_pairs = 
for nombre in liste_entiers:
  if nombre % 2 ==  0:
    nombres_pairs = nombres_pairs + 1

print("Nombre de nombre pairs:", nombres_pairs)
