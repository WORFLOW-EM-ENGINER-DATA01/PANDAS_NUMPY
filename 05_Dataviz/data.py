import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Génération de données aléatoires pour simuler les ventes de détail
def generate_retail_data(num_rows):
    # Liste des produits
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    # Liste des pays
    countries = ['France', 'Germany', 'UK', 'Spain', 'Italy']
    # Liste des clients
    customers = ['Customer 1', 'Customer 2', 'Customer 3', 'Customer 4', 'Customer 5']
    
    data = {'InvoiceNo': [],
            'InvoiceDate': [],
            'Product': [],
            'Quantity': [],
            'UnitPrice': [],
            'Country': [],
            'Customer': []}
    
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    
    for _ in range(num_rows):
        data['InvoiceNo'].append('INV' + str(random.randint(1000, 9999)))
        data['InvoiceDate'].append(start_date + timedelta(days=random.randint(0, (end_date - start_date).days)))
        data['Product'].append(random.choice(products))
        data['Quantity'].append(random.randint(1, 10))
        data['UnitPrice'].append(round(random.uniform(5, 100), 2))
        data['Country'].append(random.choice(countries))
        data['Customer'].append(random.choice(customers))
        
    return pd.DataFrame(data)

# Générer des données de vente de détail
retail_data = generate_retail_data(10000)

# Afficher un échantillon des données
print(retail_data.head())

# Enregistrer les données générées dans un fichier CSV
retail_data.to_csv('retail_sales_data.csv', index=False)
