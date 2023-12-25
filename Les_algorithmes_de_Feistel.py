
key = int(input("Entrez votre clé de 8 bits en binaire : "), 2) # Convertir la clé en entier
permutation = list(map(int, input("Entrez votre permutation de 8 chiffres : "))) # Convertir la permutation en liste d'entiers
shift = int(input("Entrez votre ordre de décalage : ")) # Convertir le décalage en entier

# Fonction pour appliquer une permutation à un bloc de bits
def permute(block, permutation):
    result = 0
    for i in range(len(permutation)):
        bit = (block >> permutation[i]) & 1 # Extraire le bit à la position permutation[i]
        result = (result << 1) | bit # Ajouter le bit au résultat
    return result

# Fonction pour appliquer un décalage circulaire à un bloc de bits
def rotate(block, size, shift):
    mask = (1 << size) - 1 # Masque pour garder les bits significatifs
    block = block & mask # Appliquer le masque au bloc
    return ((block << shift) | (block >> (size - shift))) & mask # Décaler le bloc et combiner les bits

# Fonction pour générer les sous-clés à partir de la clé principale
def generate_keys(key, permutation, shift):
    keys = []
    key = permute(key, permutation) # Appliquer la permutation initiale à la clé
    k1 = key & 0xF # Extraire les 4 bits de poids faible
    k2 = (key >> 4) & 0xF # Extraire les 4 bits de poids fort
    k1 = k1 ^ k2 # Appliquer un XOR entre k1 et k2
    k2 = k1 & k2 # Appliquer un ET logique entre k1 et k2
    for i in range(2): # Générer deux sous-clés
        k1 = rotate(k1, 4, shift) # Appliquer le décalage à k1
        k2 = rotate(k2, 4, abs(shift)) # Appliquer le décalage inverse à k2, j'ai mis la fonc abs car le shift est toujours positif 
        keys.append((k1 << 4) | k2) # Concaténer k1 et k2 pour former la sous-clé
    return keys

# Fonction pour chiffrer ou déchiffrer un bloc avec un réseau de Feistel
def feistel_cipher(block, keys, permutation, inverse_permutation, function):
    block = permute(block, permutation) # Appliquer la permutation initiale au bloc
    l = block & 0xF # Extraire la moitié gauche
    r = (block >> 4) & 0xF # Extraire la moitié droite
    for i in range(2): # Effectuer deux tours
        f = function(r, keys[i]) # Calculer la fonction F avec la moitié droite et la sous-clé
        l, r = r, l ^ f # Échanger les moitiés et appliquer un XOR
    block = (r << 4) | l # Concaténer les moitiés finales
    block = permute(block, inverse_permutation) # Appliquer la permutation finale au bloc
    return block

# Exemple d'utilisation des fonctions
inverse_permutation = [0] * 8 # Créer une liste vide pour la permutation inverse
for i in range(8): # Remplir la liste avec les indices inversés de la permutation
    inverse_permutation[permutation[i]] = i

function = lambda x, k: (x + k) % 16 # Fonction F simple

keys = generate_keys(key, permutation, shift) # Générer les sous-clés
print("Sous-clés :", [bin(k) for k in keys])

plaintext = int(input("Entrez votre texte clair de 8 bits en binaire : "), 2) # Convertir le texte clair en entier
print("Texte clair :", bin(plaintext))

ciphertext = feistel_cipher(plaintext, keys, permutation, inverse_permutation, function) # Chiffrer le texte clair
print("Texte chiffré :", bin(ciphertext))

decrypted = feistel_cipher(ciphertext, keys[::-1], permutation, inverse_permutation, function) # Déchiffrer le texte chiffré
print("Texte déchiffré :", bin(decrypted))

