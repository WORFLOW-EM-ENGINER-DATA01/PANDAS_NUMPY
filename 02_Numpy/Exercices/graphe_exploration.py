"""
 Graphe parcours

 Représentation d'un graphe

Ici on ne parle par de graphe orienté.

On peut utiliser un dictionnaire pour représenter un graphe, attention à la manière dont on implémente le graphe. Dans un dictionnaire il n'y pas de notion d'ordre. Les clés ci-dessous ne sont pas ordonnées dans le dictionnaire. Par contre les listes sont ordonnées.

Ci-dessous on définit

```python

graph = {
    'A' : [ 'B', 'C', 'D' ],
    'B' : [ 'E', 'F' ],
    'D' : [ 'G', 'H', 'I'],
    'I' : [ 'J', 'K', 'L']
}

```

Le parcours en profondeur est basé sur une pile, elle permet en dépilant d'explorer le graphe dans le sens de la profondeur. Le parcours en largeur est basé sur une queue premier entré, premier sorti permet de parcourir dans la largeur le graphe.

## Parcours en profondeur

On commence avec un noeud donné puis on explore chaque branche complètement avant de passer à la suivante. On peut dire que l'on explore à fond un noeud avant de passer au suivant. On va au plus profond dans le graphe

On peut implémenter le parcours de manière itérative ou récursive. Voyez d'abord une manière itérative :

```python

def iter_dfs(graph, node):
     Le résultat sera renvoyé dans une liste
     ce sont les noeuds visités
    visited = []
    
     On définit une queue pour visiter les noeuds
     Ceci servira à explorer le graphe
    stack = []
    
     On renregistre le noeud dans la liste pour voir
     les noeuds fils
    stack.append(node)
    
    while stack:
         le dernier rentré sera le premier sortie ou
         de manière équivalente last in first out
         L I F O
        node = stack.pop()
        
         si on ne l'a pas visité encore
         on ne doit pas le remettre une deuxième fois dans 
         les noeuds visités
        if node not in visited:
            visited.append(node)
             On vérifie que le noeud est une clé du graphe (dictionnaire)
             dans ce cas il a des fils, sinon c'est terminé on est arrivé au bout de cette
             branche
            if node in graph:
                 on récupère tous les fils du noeud
                unvisited = [ n for n in graph[node]  ]
                 puis on les met dans la pile
                stack.extend(unvisited)
                        
    return visited
```

"""

# Le code


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
                # debug
                print(stack)
                        
    return visited

print(iter_dfs(graph, 'A'))

###########################################################################


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
                # debug
                print(queue)
                        
    return visited



graph = {
    'A' : [ 'B', 'C', 'D' ],
    'B' : [ 'E', 'F'   ],
    'D' : [ 'G', 'H', 'I' ],
    'I' : [ 'J', 'K', 'L' ]
}

print(iter_bfs(graph, 'A'))