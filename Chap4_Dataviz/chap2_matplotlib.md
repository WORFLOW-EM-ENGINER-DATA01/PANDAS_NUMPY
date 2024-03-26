# Introduction à Matplotlib : Visualisation de Données en Python

## Qu'est-ce que Matplotlib ?

Matplotlib est une bibliothèque de visualisation de données en Python largement utilisée et hautement personnalisable. 
Elle permet de créer une grande variété de graphiques statiques, interactifs et complexes pour explorer et communiquer efficacement les informations contenues dans les données.

## Pourquoi utiliser Matplotlib ?

- **Flexibilité** : Matplotlib offre un contrôle complet sur la création de graphiques, vous permettant de personnaliser chaque aspect du graphique selon vos besoins.
- **Compatibilité** : Intégration transparente avec les autres bibliothèques Python telles que NumPy, Pandas et SciPy pour une manipulation facile des données.
- **Large gamme de graphiques** : De simples graphiques à barres aux graphiques tridimensionnels complexes, Matplotlib prend en charge une multitude de types de graphiques.
- **Documentation complète** : Matplotlib est bien documenté avec une vaste collection de tutoriels et d'exemples pour vous aider à démarrer rapidement.

## Les éléments clés de Matplotlib :

### 1. Figures et Axes :

- Une **figure** est la fenêtre globale dans laquelle les graphiques sont tracés.
- Un **axe (Axes)** représente une zone spécifique à l'intérieur de la figure où les données sont tracées.

### 2. Types de graphiques :

- **Graphique à barres** : Idéal pour comparer des catégories de données.
- **Graphique linéaire** : Pour visualiser les tendances et les relations entre les données.
- **Diagramme circulaire** : Utile pour représenter les parts de données dans un ensemble.
- **Histogramme** : Pour visualiser la distribution des données.

## Exemples :

### 1. Graphique à Barres :

```python
import matplotlib.pyplot as plt

# Données d'exemple
categories = ['A', 'B', 'C', 'D']
valeurs = [10, 20, 15, 25]

# Création du graphique à barres
plt.bar(categories, valeurs, color='skyblue')
plt.xlabel('Catégories')
plt.ylabel('Valeurs')
plt.title('Graphique à Barres')
plt.show()
```

### 2. Graphique Linéaire :

```python
import matplotlib.pyplot as plt

# Données d'exemple
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 16]

# Création du graphique linéaire
plt.plot(x, y, marker='o', color='green')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graphique Linéaire')
plt.show()
```

### 3. Diagramme Circulaire :

```python
import matplotlib.pyplot as plt

# Données d'exemple
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# Création du diagramme circulaire
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Diagramme Circulaire')
plt.axis('equal')  # Assure un cercle parfait
plt.show()
```

### 4. Histogramme :

```python
import matplotlib.pyplot as plt
import numpy as np

# Données d'exemple
np.random.seed(0)
data = np.random.randn(1000)

# Création de l'histogramme
plt.hist(data, bins=30, color='orange', edgecolor='black')
plt.xlabel('Valeurs')
plt.ylabel('Fréquence')
plt.title('Histogramme')
plt.show()
```

### 5. Scatter Plot (Diagramme de dispersion) :
- **Utilité** : Le diagramme de dispersion est utilisé pour visualiser la relation entre deux variables continues. Chaque point sur le graphique représente une paire de valeurs pour ces deux variables.
- **Caractéristiques** :
  - Les points sont dispersés sur le graphique, sans aucune ligne reliant les points.
  - Les points peuvent être colorés ou marqués différemment pour représenter des groupes ou des catégories supplémentaires.

#### Exemple

```python
import matplotlib.pyplot as plt
import numpy as np

# Données d'exemple
x = np.random.randn(100)
y = np.random.randn(100)

# Création du diagramme de dispersion
plt.scatter(x, y, color='red', alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Diagramme de Dispersion')
plt.show()
```

### 6. Box Plot (Diagramme en boîte) :
- **Utilité** : Le diagramme en boîte est utilisé pour visualiser la distribution d'une variable numérique et pour détecter les valeurs aberrantes (outliers).
- **Caractéristiques** :
  - Le diagramme est composé de boîtes et de lignes (ou "moustaches").
  - La boîte représente le premier quartile, la médiane et le troisième quartile de la distribution.
  - Les moustaches s'étendent aux valeurs minimales et maximales qui ne sont pas des valeurs aberrantes.
  - Les valeurs aberrantes sont représentées individuellement.

#### Exemple 

```python
import matplotlib.pyplot as plt
import numpy as np

# Données d'exemple
np.random.seed(10)
data = np.random.normal(0, 1, 100)

# Création du diagramme en boîte
plt.boxplot(data)
plt.xlabel('Données')
plt.ylabel('Valeurs')
plt.title('Diagramme en Boîte')
plt.show()
```

### 7. Violin Plot (Diagramme en violon) :
- **Utilité** : Le diagramme en violon est similaire au diagramme en boîte, mais il affiche également la distribution des données.
- **Caractéristiques** :
  - Le diagramme ressemble à un violon avec une boîte au milieu.
  - La largeur du violon représente la densité de probabilité des données à différentes valeurs.
  - Il fournit une visualisation plus détaillée de la distribution des données par rapport au diagramme en boîte.

#### Exemple

```python
import matplotlib.pyplot as plt
import numpy as np

# Données d'exemple
np.random.seed(20)
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(1, 1, 100)

# Création du diagramme en violon
plt.violinplot([data1, data2])
plt.xlabel('Groupes')
plt.ylabel('Valeurs')
plt.title('Diagramme en Violon')
plt.xticks([1, 2], ['Groupe 1', 'Groupe 2'])
plt.show()
```

### 8. Heatmap (Carte de chaleur) :
- **Utilité** : La carte de chaleur est utilisée pour visualiser des données tabulaires sous forme de couleurs. C'est utile pour identifier les schémas et les tendances dans les données.
- **Caractéristiques** :
  - Chaque cellule de la carte de chaleur est colorée en fonction de la valeur de la donnée qu'elle représente.
  - Les couleurs peuvent être graduelles pour représenter une plage de valeurs ou discrètes pour représenter des catégories.

#### Exemple

```python
import matplotlib.pyplot as plt
import numpy as np

# Données d'exemple
np.random.seed(0)
data = np.random.rand(10, 10)

# Création de la carte de chaleur
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Carte de Chaleur')
plt.show()
```

### 9. Surface Plot (Graphique de surface) :

- **Utilité** : Le graphique de surface est utilisé pour visualiser les relations tridimensionnelles entre trois variables continues.
- **Caractéristiques** :
  - Il représente une surface tridimensionnelle où la hauteur de la surface représente la valeur de la troisième variable.
  - Il est souvent utilisé pour visualiser des fonctions mathématiques ou des ensembles de données tridimensionnels.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Données d'exemple
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Création du graphique de surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
ax.set_title('Graphique de Surface')
plt.show()
```