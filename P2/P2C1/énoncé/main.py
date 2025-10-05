nombre1 = input("Entrer un nombre entier: ")
nombre2 = input("Entrer un nombre entier: ")

# utilisation de la méthode isnumeric
if not nombre1.isnumeric() or not nombre2.isnumeric()
      print("Errer: Les deux doivent être des nombres entiers")
raise systemExit("Fin de programme")

nombre1 = int(nombre1)
nombre2 = int(nombre2)

operation = input("Entrer l'opération souhaiter['+','-','/','*']: ")

if operation is not  in ['+','-','/','*']
      print("Errer: le symbole doit être '+','-','/','*'")
raise systemExit("Fin de programme")


if opertion == '-'
   resultat = nombre1 - nombre2
elif operation  == '*'
   resultat = nombre1 * nombre2
elif operation == '/'
   resultat = nombre1 / nombre2
elif operation == '+'
   resultat = nombre1 + nombre2

#vérifier si le "nombre2" n'est pas nul pour la division

if nombre2 = 0
   print("Errer: Impossible de diviser par zéro")
raise systemExit("Fin de programme")

resultat = round(nombre1 / nombre2, 2)

#Afficher le resultat

print(f"Le résultat de l'operation: {round(nombre1 / nomlbre2, 2)}")
