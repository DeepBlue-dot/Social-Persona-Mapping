import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


class StructuralSimilarity:
    """
    Computes structural similarity between two images.
    """

    def load_gray(self, path: str):
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        return img

    def ssim_score(self, img1, img2) -> float:
        if img1 is None or img2 is None:
            return 0.0
        img2 = cv2.resize(img2, img1.shape[::-1])
        score, _ = ssim(img1, img2, full=True)
        return float(score)

    def histogram_score(self, img1, img2) -> float:
        if img1 is None or img2 is None:
            return 0.0

        hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
        hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
        cv2.normalize(hist1, hist1)
        cv2.normalize(hist2, hist2)

        return float(cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL))

    def edge_similarity(self, img1, img2) -> float:
        if img1 is None or img2 is None:
            return 0.0

        edges1 = cv2.Canny(img1, 100, 200)
        edges2 = cv2.Canny(img2, 100, 200)

        intersection = np.logical_and(edges1, edges2).sum()
        union = np.logical_or(edges1, edges2).sum()

        return float(intersection / union) if union > 0 else 0.0

    def compare(self, path1: str, path2: str) -> float:
        img1 = self.load_gray(path1)
        img2 = self.load_gray(path2)

        ssim_v = self.ssim_score(img1, img2)
        hist_v = self.histogram_score(img1, img2)
        edge_v = self.edge_similarity(img1, img2)

        return round(
            0.5 * ssim_v +
            0.3 * hist_v +
            0.2 * edge_v,
            4
        )
