import numpy as np
import json


class Vectors:
    def __init__(self):
        with open('cosine_similarity/vectors.json') as f:
            self.vector_dict = json.loads(f.read())

    def get_vector(self, name: str) -> np.ndarray:
        return np.array(self.vector_dict[name])