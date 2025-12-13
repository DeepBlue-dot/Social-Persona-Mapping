import torch
import numpy as np
from PIL import Image
import open_clip


class OpenCLIPModel:
    """
    Extracts full-image embeddings using OpenCLIP.
    """

    def __init__(
        self,
        model_name: str = "ViT-B-32",
        pretrained: str = "laion2b_s34b_b79k",
        device: str = "cpu",
    ):
        self.device = device
        self.model, _, self.preprocess = open_clip.create_model_and_transforms(
            model_name, pretrained=pretrained
        )
        self.model.to(device)
        self.model.eval()

    def extract(self, image_path: str) -> np.ndarray | None:
        try:
            image = Image.open(image_path).convert("RGB")
        except Exception:
            return None

        image = self.preprocess(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            embedding = self.model.encode_image(image)

        embedding = embedding / embedding.norm(dim=-1, keepdim=True)
        return embedding.squeeze(0).cpu().numpy()
