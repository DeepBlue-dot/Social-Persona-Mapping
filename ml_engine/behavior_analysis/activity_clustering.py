import numpy as np
from sklearn.cluster import KMeans, DBSCAN
from typing import Literal


class ActivityClustering:
    """
    Clusters behavioral vectors to detect usage patterns.
    """

    def __init__(self, method: Literal["kmeans", "dbscan"] = "kmeans"):
        self.method = method

    def cluster(self, vectors: np.ndarray, n_clusters: int = 2) -> np.ndarray:
        if len(vectors) == 0:
            return np.array([])

        if self.method == "kmeans":
            model = KMeans(n_clusters=n_clusters, random_state=42)
            return model.fit_predict(vectors)

        if self.method == "dbscan":
            model = DBSCAN(eps=0.5, min_samples=2)
            return model.fit_predict(vectors)

        raise ValueError("Unsupported clustering method")

    def summarize_clusters(self, labels: np.ndarray) -> dict:
        unique, counts = np.unique(labels, return_counts=True)
        return dict(zip(unique.tolist(), counts.tolist()))
