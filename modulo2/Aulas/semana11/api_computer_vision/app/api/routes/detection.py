from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import Response
from app.services.detection import predict_to_yolo_format
import os

router = APIRouter(
    prefix="/detection",
    tags=["Datecção de objetos"]
)

@router.post("/copos-garrafas",summary="Detecta copos e ggarrafas dse uma imagem")
async def detect_objects(file: UploadFile= File(...), yolo_version: str = "v8" ):
# Valida imagem
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="O arquivo não é uma umagem!")
    try:
        # Ler bytes do arquivo
        image_bytes = await file.read()
        # chamar serviço
        txt_context = predict_to_yolo_format(image_bytes,yolo_version) 
        # Extrair o nome original da imagem e trocar a extensão para .txt
        nome_original = file.filename
        nome_base = os.path.splitext(nome_original)[0]
        nome_txt = f"{nome_base}.txt"
        
        return Response (
            content= txt_context,
            media_type="text/plain",
            headers={"Content-Disposition": f'attachment; filename="{nome_txt}"'}
        )

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro durante a inferencia: {str(e)}')
