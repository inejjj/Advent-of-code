fichier = open("adventcode1.txt", "r")

calcul = []

for f in fichier :
  bonne_ligne = []
  for n in f :
    if n.isdigit():
      bonne_ligne.append(n)
  ultime = bonne_ligne[0] + bonne_ligne[-1]
  new_ultime = int(ultime)
  calcul.append(new_ultime)

print(sum(calcul))