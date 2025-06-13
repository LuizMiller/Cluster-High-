import torch
import clip
from PIL import Image

model, preprocess = clip.load("ViT-B/32")
image1 = preprocess(Image.open("img1.jpg")).unsqueeze(0)
image2 = preprocess(Image.open("img2.jpg")).unsqueeze(0)

with torch.no_grad():
    emb1 = model.encode_image(image1)
    emb2 = model.encode_image(image2)

similarity = torch.cosine_similarity(emb1, emb2)
print("Similaridade semântica:", similarity.item())
