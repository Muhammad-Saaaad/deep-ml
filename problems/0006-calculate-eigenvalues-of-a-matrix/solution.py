import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

	eign_values, eign_vectors = np.linalg.eig(matrix)
	return list(eign_values)