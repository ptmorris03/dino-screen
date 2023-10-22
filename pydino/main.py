# Load model directly
from transformers import AutoFeatureExtractor, AutoModel

extractor = AutoFeatureExtractor.from_pretrained("facebook/dinov2-large")
model = AutoModel.from_pretrained("facebook/dinov2-large")

