import numpy as np
from .data_access import Vectors


class Similarity:
    def __init__(self):
        self.vectores = Vectors()

    def calculate_similarity(self, name1: str, name2: str) -> float:
        vector1 = self.vectores.get_vector(name1)
        vector2 = self.vectores.get_vector(name2)

        if vector1.shape != vector2.shape:
            raise ValueError("Vectors must have the same shape")

        if vector1.ndim != 1 or vector2.ndim != 1:
            raise ValueError("Vectors must be 1-dimensional")

        if vector1 is None or vector2 is None:
            raise ValueError("Vectors cannot be None")

        return np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))