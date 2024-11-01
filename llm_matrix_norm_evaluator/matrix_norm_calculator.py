
import numpy as np

class MatrixNormCalculator:
    def __init__(self, config):
        self.config = config

    def l1_2_norm(self, matrix):
        if matrix.shape[0] > 1000:
            print("Warning: Large matrix detected. Consider processing in batches.")
        row_norms = np.linalg.norm(matrix, axis=1)
        return np.linalg.norm(row_norms, 1)

    def matrix_nuclear_norm(self, matrix):
        """Calculate the matrix nuclear norm."""
        return np.linalg.norm(matrix, ord='nuc')
    