# Fonction pour calculer x^b (mod n) en utilisant l'algorithme des carrés et des multiplications
def square_multiply(x, b, n):
  # Convertir b en binaire
  b = bin(b)[2:]
  # Initialiser le résultat à 1
  result = 1
  # Parcourir les bits de b de droite à gauche
  for bit in b[::-1]:
    # Si le bit est 0, on élève le résultat au carré
    if bit == "0":
      result = (result * result) % n
    # Si le bit est 1, on élève le résultat au carré et on le multiplie par x
    else:
      result = (result * result * x) % n
  # Retourner le résultat final
  return result

# Demander à l'utilisateur d'entrer les valeurs de x, b et n
x = int(input("Entrez la valeur de x: "))
b = int(input("Entrez la valeur de b: "))
n = int(input("Entrez la valeur de n: "))

# Appeler la fonction square_and_multiply et afficher le résultat
print(f"{x}^{b} (mod {n}) = {square_multiply(x, b, n)}")



