import cv2
import numpy as np

from fastapi import HTTPException
from insightface.app import FaceAnalysis
from sklearn.metrics.pairwise import cosine_similarity

app = FaceAnalysis(provider=['CPUExecutionProvider'])
app.prepare(ctx_id=0)

def compare_faces(img1_byt, img2_byt):
    img1 = cv2.imdecode(
        np.frombuffer(img1_byt, np.uint8),
        cv2.IMREAD_COLOR
    )

    img2 = cv2.imdecode(
        np.frombuffer(img2_byt, np.uint8),
        cv2.IMREAD_COLOR
    )

    faces1 = app.get(img1)
    faces2 = app.get(img2)

    if len(faces1) == 0:
        raise HTTPException(
            status_code = 400,
            detail = "error: no face detected in image 1"
        )
        
    
    if len(faces2) == 0:
        raise HTTPException(
            status_code = 400,
            detail = "error: no face detected in image 2"
        )
    
    face1 = faces1[0]
    face2 = faces2[0]

    similarity = cosine_similarity(
        [face1.embedding],
        [face2.embedding]
    )[0][0]

    similarity_percentage = float(round(similarity * 100, 2))

    threshold = 50

    result = ("Same person" if similarity_percentage > threshold else "Different Person")

    return {
        "Verification_result": result,
        "Similarity_score": round(similarity_percentage, 4),
        "Face1_Bounding_Box": face1.bbox.tolist(),
        "Face2_Bounding_Box": face2.bbox.tolist()
    }
        

    