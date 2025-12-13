import numpy as np
import cv2
from insightface.app import FaceAnalysis


class InsightFaceModel:
    """
    Extracts face embeddings using InsightFace.
    """

    def __init__(self, ctx_id: int = 0, det_size=(640, 640)):
        self.app = FaceAnalysis(name="buffalo_l")
        self.app.prepare(ctx_id=ctx_id, det_size=det_size)

    def extract(self, image_path: str) -> np.ndarray | None:
        img = cv2.imread(image_path)
        if img is None:
            return None

        faces = self.app.get(img)
        if not faces:
            return None

        # Take the largest detected face
        face = max(faces, key=lambda f: f.bbox[2] * f.bbox[3])
        return face.normed_embedding  # (512,)
