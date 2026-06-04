from fastapi import FastAPI, File, UploadFile
from services.face_service import compare_faces

app = FastAPI(
    title="Face Authentication API",
    description="Verify whether two uploaded images belong to the same person.",
    version="1.0"
)

@app.get("/")
def home():
    return {"message": "Face Authentication API running"}

@app.post("/compare-face")
async def compare_face(
    img1: UploadFile = File(...),
    img2: UploadFile = File(...)
):
    
    img1_byt = await img1.read()
    img2_byt = await img2.read()

    result = compare_faces(
        img1_byt,
        img2_byt
    )

    return result