import numpy as np
from typing import Dict


class ImageComparator:
    """
    Combines face, CLIP, and structural similarity into a final score.
    """

    def cosine_similarity(self, a: np.ndarray, b: np.ndarray) -> float:
        if a is None or b is None:
            return 0.0
        if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
            return 0.0
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

    def compare(
        self,
        face_emb_1: np.ndarray | None,
        face_emb_2: np.ndarray | None,
        clip_emb_1: np.ndarray | None,
        clip_emb_2: np.ndarray | None,
        structure_score: float,
    ) -> Dict:
        face_sim = self.cosine_similarity(face_emb_1, face_emb_2)
        clip_sim = self.cosine_similarity(clip_emb_1, clip_emb_2)

        final_score = round(
            0.5 * face_sim +
            0.3 * clip_sim +
            0.2 * structure_score,
            4
        )

        return {
            "face": round(face_sim, 4),
            "clip": round(clip_sim, 4),
            "structure": round(structure_score, 4),
            "final_score": final_score,
        }
