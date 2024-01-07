import random

a = random.randint(1, 10)
y = int(input("choisissez un chiffre entre 1 et 9 "))
if a == y:
    print("bravo vous avez trouvé directement le bon chiffre égale à", a )
elif a != y:
    y = int(input("je vous laisse une seconde chance !"))
elif a != y:
        print("dommage le chiffre à trouver est "+str(a))
else:
    print("bien joué le chiffre à trouver est bien "+str(a))

        

# trouver un nombre aléatoire #


