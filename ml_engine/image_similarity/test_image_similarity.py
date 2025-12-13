
from ml_engine.image_similarity.insightface_model import InsightFaceModel
from ml_engine.image_similarity.openclip_model import OpenCLIPModel
from ml_engine.image_similarity.structural_similarity import StructuralSimilarity
from ml_engine.image_similarity.image_comparator import ImageComparator

# Paths
img1 = "data/test_images/user1/profile.jpg"
img2 = "data/test_images/user2/profile.jpg"

# Initialize models
face_model = InsightFaceModel(ctx_id=0)
clip_model = OpenCLIPModel(device="cpu")
structure_model = StructuralSimilarity()
comparator = ImageComparator()

# Extract embeddings
face_emb_1 = face_model.extract(img1)
face_emb_2 = face_model.extract(img2)

clip_emb_1 = clip_model.extract(img1)
clip_emb_2 = clip_model.extract(img2)

structure_score = structure_model.compare(img1, img2)

# Compare
result = comparator.compare(
    face_emb_1=face_emb_1,
    face_emb_2=face_emb_2,
    clip_emb_1=clip_emb_1,
    clip_emb_2=clip_emb_2,
    structure_score=structure_score
)

print("\n🔍 IMAGE SIMILARITY RESULT")
print(result)
