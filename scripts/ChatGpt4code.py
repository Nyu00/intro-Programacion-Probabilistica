import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generar datos de ejemplo
X, y_true = make_blobs(n_samples=100, centers=3, random_state=0)

# Crear el objeto de agrupamiento jerárquico
clustering = AgglomerativeClustering(n_clusters=3)

# Ajustar el modelo a los datos
clustering.fit(X)

# Obtener las etiquetas de los clusters asignados a cada muestra
labels = clustering.labels_

# Plotear los resultados
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.title('Agrupamiento jerárquico')
plt.show()
