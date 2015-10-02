
 **Cryptographie Avancée : Problème du chèque**
---

*Description rapide du problème :*
>Nous avons 3 acteurs : un client, un commerçant, une banque.
Comment faire en sorte qu’une transaction commerciale grave à un chèque puisse être effectuée, en supposant par exemple que ni le client, ni le commerçant ne peuvent contacter la banque pendant l’achat (les deux sont dans un avion), et cela sans qu’aucun acteur ne puisse tricher sur les autres ?
(nous ne traiterons pas du sujet d’un chèque en bois dans ce cas)


##Traitement du problème

Présomption de départ : le client doit avoir sa clé publique signée par la banque (par exemple à son adhésion à la banque)

La transaction se fait de façon active (échange entre les acteurs).

Le chèque contient 3 informations principales :
 - Le chiffrement par le client de la clé publique du commerçant
 - Le chiffrement par la banque de la clé publique du client  
 - La somme de la transaction (en nombre entier)
 - Un numéro unique généré par le commerçant pour vérifier que le chèque ne soit pas copié par un client malveillant

Lors de la fin de la transaction, le commerçant aura le chèque vérifié avec la facture

Quand la banque reçoit le chèque, la banque signera le chèque et le gardera en mémoire afin de pouvoir garantir l’unicité des chèques => un chèque sera viré une et une fois seulement par la banque

----

## Problèmes à résoudre
1. Comment le commerce peut-il être sur que le client est bien de la banque qu’il indique ?

-> Signature de la clé publique du client par la banque, à la présentation du chèque, le commerce donc peut utiliser la clée publique de la banque pour vérifier l’appartenance du client à la banque

2. Comment la banque peut-elle vérifier que le chèque que le commerce lui donne vient bien du client ?

-> La signature du chèque par le client

3. Comment empêcher au commerce de faire une copie du chèque et ensuite la donner à la banque ?

-> Signature du chèque par la banque

4. Comment empêcher la banque d’indiquer au commerce que le chèque a une valeur différente de ce que le commerce en attend ?

-> Cf. 2 : Le client aura vérifié également la somme et signé le chèque

----

## Création d’une preuve de concept

>Langage utilisé : Python (3.4)

5 programmes principaux à créer :

1. Initialisation
  - Génération clé publique/privée banque
  - Génération clé publique/privée client
  - Génération clé publique/privée commerçant
  - Chiffrer la clé publique du client avec la clé privée de la banque :
2. Programme du commerçant
  - Génération d’une facture contenant :
  - Id (UUID par exemple)
  - Somme
  - Information sur le produit
3. Programme du client qui prend en paramètre la facture et va produire le chèque :
  - Clé publique du commerçant chiffrée par le client
  - Clé publique du client chiffrée par la banque
  - Somme de la transaction et numéro unique chiffrés
4. Programme du commerçant : prend facture et le chèque et répond si c’est ok ou pas
  - Vérifie que les données a. et b. de 3. n’ont pas été altérées par le client
5. Programme de la banque : va prendre chèque et effectue la transaction (ou pas)
  - S’assure que le chèque n’est pas une copie d’un chèque déjà déposé
  - Vérifie que le chèque a bien été chiffré par le client
