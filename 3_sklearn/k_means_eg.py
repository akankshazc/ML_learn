from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Load the Iris dataset
iris = load_iris()

# Initialize the KMeans clustering model
kmeans = KMeans(n_clusters=3)

# Fit the model to the data
kmeans.fit(iris.data)

# Get the cluster labels
cluster_labels = kmeans.labels_

print("Cluster Labels:", cluster_labels)
