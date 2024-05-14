import numpy as np

## Exercice 1

g1 = np.array([
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
       [0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
       [1, 1, 1, 0, 0, 0, 1, 0, 1, 0],
       [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
       [0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
       [0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
       [0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
       [1, 1, 1, 1, 1, 1, 0, 0, 1, 0]
    ])

"""
Dans la matrice ci-dessus, un sommet est représenté par une ligne. Cette matrice
représente les intérêts que des personnes peuvent avoir l'une pour l'autre. Il y a 
parfois réciprocité.

Si (l,c) vaut 1 alors cette personne est intéressée par la personne (c,l), il y a 
réciprocité dans la relation d'intérêt si (c, l) vaut 1.

- Cherchez toutes les réciprocités du tableau pour former les couples de personne(s)
qui partage un intérêt commun.
"""

## Exercice 2
"""

Parcours en profondeur
"""

graph = {
    'A' : [ 'B', 'C', 'D' ],
    'B' : [ 'E', 'F'   ],
    'D' : [ 'G', 'H', 'I' ],
    'I' : [ 'J', 'K', 'L' ]
}

# On choisit un noeud

"""

depth first search

"""

def iter_dfs(graph, node):
    # Le résultat sera renvoyé dans une liste
    # ce sont les noeuds visités
    visited = []
    
    # On définit une queue pour visiter les noeuds
    # Ceci servira à explorer le graphe
    stack = []
    
    # On enregistre le noeud dans la liste pour voir
    # les noeuds fils
    stack.append(node)
    
    while stack:
        # le dernier rentré sera le premier sortie ou
        # de manière équivalente last in first out
        # L I F O
        node = stack.pop()
        
        # si on ne l'a pas visité encore
        # on ne doit pas le remettre une deuxième fois dans 
        # les noeuds visités
        if node not in visited:
            visited.append('-->' + node)
            # On vérifie que le noeud est une clé du graphe (dictionnaire)
            # dans ce cas il a des fils
            if node in graph:
                # on récupère tous les fils du noeud
                unvisited = [ n for n in graph[node]  ]
                # puis on les met dans la pile
                stack.extend(unvisited)
                print(stack)
                        
    return visited

print(iter_dfs(graph, 'A'))

"""
Parcours en largeur

"""

def iter_bfs(graph, node):
    # Le résultat sera renvoyé dans une liste
    # ce sont les noeuds visités
    visited = []
    
    # On définit une queue pour visiter les noeuds
    # Ceci servira à explorer le graphe
    queue = []
    
    # On enregistre le noeud dans la liste pour voir
    # les noeuds fils
    queue.append(node)
    
    while queue:
        # le premier entré est le premier sorti
        # de manière équivalente first in first out
        # F I F 0
        node = queue[0]
        queue = queue[1:]
        
        # si on ne l'a pas visité encore
        # on ne doit pas le remettre une deuxième fois dans 
        # les noeuds visités
        if node not in visited:
            visited.append('-->' + node)
            # On vérifie que le noeud est une clé du graphe (dictionnaire)
            # dans ce cas il a des fils
            if node in graph:
                # on récupère tous les fils du noeud
                unvisited = [ n for n in graph[node]  ]
                # puis on les met dans la pile
                queue.extend(unvisited)
                print(queue)
                        
    return visited



graph = {
    'A' : [ 'B', 'C', 'D' ],
    'B' : [ 'E', 'F'   ],
    'D' : [ 'G', 'H', 'I' ],
    'I' : [ 'J', 'K', 'L' ]
}

print(iter_bfs(graph, 'A'))


## Exercice 3

g = np.array([
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
])

"""
Trois personnes sont des amis si ces trois personnes sont reliées dans un graphe.

- Créez une fonction qui s'appliquera sur le graphe g et testera si (1,2,3) est un triplet d'amis.

- Créez une autre fonction qui testera si un triplet (a,b,c) sont étrangés, c'est-à-dire non relié dans le graphe.

- Créez une fonction qui permet maintenant de trouver tous les triplets (a,b,c) parmi un graphe de 5 sommets.

- Puis cherchez tous les amis possibles dans la matrice ci-dessus.

"""