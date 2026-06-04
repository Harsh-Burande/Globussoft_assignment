import cv2
from insightface.app import FaceAnalysis
from sklearn.metrics.pairwise import cosine_similarity

import warnings
warnings.filterwarnings("ignore")

# Model Loading
app = FaceAnalysis(providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0)

# Images Read
img1 = cv2.imread('car.jfif')
img2 = cv2.imread('harsh2.jpg')

# detecting faces
face1 = app.get(img1)
face2 = app.get(img2)

if len(face1) == 0 or len(face2) == 0:
    print("No face detected in one of the images.")
    exit()

# detected face
face1 = face1[0]
face2 = face2[0]

# Bounding Box
print("Face 1 Bounding Box:", face1.bbox.tolist())
print("Face 2 Bounding Box:", face2.bbox.tolist())

# Face embeddings
embd1 = face1.embedding
embd2 = face2.embedding

# Cosine similarity
similarity = cosine_similarity(
    [embd1],
    [embd2]
)[0][0]

threshold = 0.50
if similarity > threshold:
    result = "Faces are similar."
else:
    result = "Faces are not similar."

print(f"Result: {result}")
print(f"Similarity Score: {similarity:.4f}")