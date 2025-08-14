from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

# Load the digits dataset
digits = load_digits()

# Initialize PCA for dimensionality reduction
pca = PCA(n_components=2)

# Apply PCA to the data
reduced_data = pca.fit_transform(digits.data)

print("Original data shape:", digits.data.shape)
print("Reduced data shape:", reduced_data.shape)
