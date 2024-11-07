import kagglehub

# Download latest version
path = kagglehub.dataset_download(r"uciml/breast-cancer-wisconsin-data")

print("Path to dataset files:", path)