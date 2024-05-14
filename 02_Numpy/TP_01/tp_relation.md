# TP exploration de données

Pour ce TP qui est un TP de recherche de relations dans un dataset vous pouvez me contacter pour de l'aide sur slack pendant les vacances. N'hésites pas. Notamment si vous êtes bloqué je peux vous aidez à trouver des éléments de script qui vous permettrons d'avancer. Sur Slack dans ce cas posez moi votre question, j'y répondrais dès que possible en vous donnant des conseils et exemples.

Pour le développement vous devez créer un notebook et si vous le souhaitez un fichier que vous importez dans votre notebook qui contiendra vos scripts.

Avant de commencer ci-dessous vous avez une partie **Partie les données de l'exercice**. Ce sont les données à explorer.

## Partie les données de l'exercice

```python

populations = [
    { "id" : 0, "name" : "Alan" },
    { "id" : 1, "name" : "Albert" },
    { "id" : 2, "name" : "Jhon" },
    { "id" : 3, "name" : "Brice" },
    { "id" : 4, "name" : "Alexendra" },
    { "id" : 5, "name" : "Brad" },
    { "id" : 6, "name" : "Carl" },
    { "id" : 7, "name" : "Dallas" },
    { "id" : 8, "name" : "Dennis" },
    { "id" : 9, "name" : "Edgar" },
    { "id" : 10, "name" : "Erika" },
    { "id" : 11, "name" : "Isaac" },
    { "id" : 12, "name" : "Ian" }
]

relationships = [
    (0,1), (0,2), (1,2), (1,4),(2,3), (2,5),
    (3,4), (3,7), (4,5),(4,8), (4,9), (5,7),
    (5,9), (6,7), (6,8), (7,1), (7,8), (8,9),
    (10,1),(10,2),(10,3),(11,12),(11,2),(11,5)
]

```

## Partie 1 préparation des données

Vous avez les données suivantes une liste de dictionnaires et une liste de tuples relationships. Chaque personne de cette population est identifiée par l'indice de la liste. Ainsi Alan dans la liste population est atteignable en utilisant l'indice 0 sur cette liste.

Dans un premier temps parcourez la liste populations et ajoutez une clé "relation" au dictionnaire pour chaque personne :

```python
for pop in populations:
    pop['relation'] = []

```

## Partie 2 ajout des relations à la liste populations

Ajoutez à la liste populations pour chaque personne l'ensemble ses relations. Les relations de chaque personne sont précisées dans la liste relationships par des couples de deux valeurs (tuples), par exemple (0,1) dans cette liste indique que Alan est en relation avec Albert, et réciproquement.

Voyez l'exemple qui suit pour Alan nous aimerions avoir dans la liste populations les relations de chaque personne sous la forme qui suit :

```python
print( populations[0] )
"""
{'id': 0, 'name': 'Alan', 'relation': ['Albert', 'Jhon']}
"""
 ```

## Partie 3 répondre aux questions sur les données

1. Calculer la moyenne des relations. Vous pouvez utiliser len, une méthode qui permet de calculer la longueur d'une liste.

2. Créez une liste représentant les users (id) et le nombre derelation(s) qu’ils possèdent. Par exemple vous pouvez ajoutez à cette liste un tuple constitué de l'id de l'utilisateur et le nombre de ses relations : (id, nb_relation)
