# Creation d'un dictionnaire
Fruits = {"pomme" : "rouge", "banane" : "jaune", "orange" : "orange"}

# Ajouter la clé kiwi
Fruits['kiwi'] = "vert"

# Acceder a la valeur Banane et stocker dans une variable_couleur
variable_couleur = Fruits["banane"]

# Modification
Fruits["pomme"] = "vert"

# Suppression 
del Fruits["banane"]

# Affichage des clés restantes
print(Fruits.key())
