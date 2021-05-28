"""
###################################################### REGLES DU JEU (Tout les mots entre '' sont des noms de variables déjà définies) ######################################################

 Vous avez un 'capital' de 100€ de départ, l'objectif pour gagner est d'atteindre 10.000€ le plus rapidement possible (avec le moins de 'nb_tours' possible)
 A chaque début de tour, on obtient un coeficient multiplicateur qui est un nombre flotant compris entre 1 et 3 stocké dans la variable 'coef_multiplicateur'
 Ce sera ensuite à vous de coder votre IA afin de définir le montant de votre 'mise' que vous devrez stocker dans la variable 'mise' (à partir de la ligne 68)
 Une fois que votre IA à définis une 'mise', la roulette tourne, si elle tombe sur 0 vous perdez votre mise, si elle tombe sur 1, vous gagnez de l'argent en fonction du coef multiplicateur, le résultat de la roulette est stocké dans la variable 'roulette' 
 Exemple : Si le coef multiplicateur est de 2 et que votre IA décide de miser 100€, si la roulette tombe sur 1, 100€ seront ajoutés à votre 'capital'
 Exemple2 : Si le coef multiplicateur est de 1 et que votre IA décide de miser 100€, si la roulette tombe sur 1, vous récupérer votre mise donc vous ne gagnez rien, par contre si la roulette tombe sur 0 vous perdez votre mise de 100€ peut importe le coef multiplicateur

 Si votre 'mise' est supérieure à votre 'capital', vous perdez
 Si votre 'mise' est inférieure à 1, vous perdez (Vous devez donc miser au minimum 1€ tout les tours même si le coef multiplicateur n'est pas avantageux pour vous)
 Si votre  IA atteint les 2000 'nb_tours', vous perdez
 Si votre 'capital' descend à 0, vous perdez
 Si votre 'capital' atteint le 'capital_objectif' (c'est à dire 10000), vous GAGNEZ !

 C'est bien beau de gagner mais comme dit précédemment, il vous faudra y arriver avec le moins de 'nb_tours' possible
 Si vous gagnez (donc que votre 'capital' atteint 'capital_objectif') vous gagnez autant de points que de 'nb_tours'
 Si vous perdez, peut importe votre 'nb_tours' et peut importe votre façon de perdre, vous gagnez 2000 points
 L'objectif est donc d'avoir une IA qui gagne le plus souvent possible avec le MOINS de points possible

 Vous avez uniquement le droit de coder votre IA dans la partie spécifiée (à partir de la ligne 68)
 Vous avez uniquement le droit de modifier la variable 'mise' parmis les variables déjà codées (mais si besoin vous pouvez en créer de nouvelles dans la partie spécifiée)
 Vous pouvez vous servir de toutes les variables pour des conditions/boucles etc tant que vous ne les modifiés pas (sauf pour 'mise' que vous devez modif du coup)
 Vous pouvez modifier dans la CONFIG les variables 'logs' et 'nb_simus' ligne 40 pour vos tests

 Une fois que vous serez satisfait de votre IA, vous m'enverez votre code sur discord (seulement la partie de votre IA et son nom sera utilisé)

 Puis un tournois entre toutes les IA aura lieu, le tournois se déroulera en 20 simulations (histoire de laisser un peu d'aléatoire)
 Le tournois sera suivis par un bot discord qui enverra dans un channel spécifique le résultat des points de chaque participant pour chaque simulation (quelques secondes entre chaque simu)
 Une fois les 20 simulations éffectuées, la moyenne des 20 simus pour chaque participant sera calculée et le classement se fera de la plus basse moyenne à la plus haute

 N'hésitez pas à lancer le script avant de commencer à coder pour mieux comprendre comment il fonctionne
 PS: Au plus le 'coef_multiplicateur' est élevée, au plus vos gains sont importants (si la 'roulette' tombe sur 1 bien sur), basez vous sur ça pour que votre IA gère le montant de votre 'mise'

 HAVE FUN & GOOD LUCK (dsl pr les fautes)
"""


############### CONFIG ###############
IA_nom = "votre ia"  # nom de votre IA ?
logs = True #Désactivez les logs si vous voulez que le script soit plus rapide   True : ON / False : OFF
nb_simus = 1 #Nombre de simulation que vous voulez faire    Mettre logs = False si vous faites bcp de simus
############# FIN CONFIG #############




from random import *
from statistics import *

nb_loose = 0
points = []

for simu_id in range(1,nb_simus+1):
    capital = capital_depart = 100
    capital_objectif = 10000
    mise, nb_tours = 0, 0

    while capital > 0 and capital < capital_objectif:
        nb_tours += 1 #on compte le nb de tours
        coef_multiplicateur = uniform(1, 3) #on génère aléatoirement un coef multiplicateur entre 1 et 3 qui est un nombre flotant





        ############################## CODEZ VOTRE IA CI-DESSOUS ##############################





        mise = 50





        ############################## CODEZ VOTRE IA CI-DESSUS ##############################



        
        if mise > capital:
            if logs is True:
                print(f"tour : {nb_tours} >> Vous n'avez pas respecté les règles, votre mise de {round(mise,2)}€ est supérieure à votre capital de {round(capital,2)}€, votre argent restant vous a été confisqué.")
            capital = 0
        elif mise < 1:
            if logs is True:
                print(f"tour : {nb_tours} >> Vous n'avez pas respecté les règles, votre mise de {round(mise,2)}€ est inférieure à 1€, votre argent restant vous a été confisqué.")
            capital = 0
        elif nb_tours == 2000:
            if logs is True:
                print(f"tour : {nb_tours} >> Vous avez dépassé le nombre limite de tours fixé à 2000, votre argent restant vous a été confisqué.")
            capital = 0
        else:
            roulette = getrandbits(1) #On lance la roulette
            capital += (mise*coef_multiplicateur*roulette)-mise #On met à jour notre nouveau capital en fonction de l'argent gagné ou perdus
            if logs is True:
                print(f"tour : {nb_tours} - Roulette : {roulette} | Coef : {round(coef_multiplicateur,2)} | Mise : {round(mise,2)}€ | gains/pertes : {round((mise*coef_multiplicateur*roulette)-mise,2)}€ | Nouv capital : {round(capital,2)}€")

    if capital >= capital_objectif:
        points.append(nb_tours)
        if logs is True:
            print("-"*100,f"\nFélicitation, {IA_nom} a atteint un capital de {round(capital,2)}€ en {nb_tours} tours, vous gagnez {nb_tours} points !")
    else:
        points.append(2000)
        nb_loose += 1
        if logs is True:
            print("-"*100,f"\nDommage, {IA_nom} a perdus votre capital en {nb_tours} tours, vous gagnez {2000} points !")

print("-"*100,f"\nVous avez fait {len(points)} simulations ({len(points)-nb_loose} gagnés / {nb_loose} perdus), la moyenne de vos points est de : {int(mean(points))}\nEssaie d'améliorer ton IA pour faire mieux !")