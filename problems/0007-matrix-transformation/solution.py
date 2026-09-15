import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	
	try:


		T = np.array(T)
		A = np.array(A)
		S = np.array(S)

		np.linalg.inv(S)

		t_inverse = np.linalg.inv(T)
		AS = A @ S
		transformed_matrix = t_inverse @ AS
		return transformed_matrix
	except:
		return -1