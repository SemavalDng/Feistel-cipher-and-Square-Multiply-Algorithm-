# Fonction pour calculer x^b (mod n) en utilisant l'algorithme des carrés et des multiplications
def square_multiply(x, b, n):
  # Coversion de b en binaire
  b = bin(b)[2:]
  result = 1
  # Parcourir les bits de b de droite à gauche
  for bit in b[::-1]:
    # on élève le résultat au carré dans le cas où le bit est 0
    if bit == "0":
      result = (result * result) % n
    #  élèvons le résultat au carré et on le multiplie par x dans le cas où le bit est 1
    else:
      result = (result * result * x) % n
  return result
x = int(input("Entrez x: "))
b = int(input("Entrez b: "))
n = int(input("Entrez n: "))
# Appeler la fonction square_multiply et afficher le résultat
print(f"{x}^{b} (mod {n}) = {square_multiply(x, b, n)}")



