import cv2
from insightface.app import FaceAnalysis

# Load insightFace model
app = FaceAnalysis()
app.prepare(ctx_id=0)

img = cv2.imread('WhatsApp Image 2026-02-11 at 12.25.04.jpeg')

faces = app.get(img)

print(f"Face dected {len(faces)}")

for idx, face in enumerate(faces):
    print(f"\nFace {idx+1}")

    print("Bounding Box")
    print(face.bbox)

    print("\nEmbedding Shape")
    print(face.embedding.shape)