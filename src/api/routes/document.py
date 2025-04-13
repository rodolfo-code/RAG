from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from pydantic import BaseModel
from uuid import uuid4

from ...domain.models import Document

class DocumentResponse(BaseModel):
    """Modelo para resposta de um documento."""
    id: str
    filename: str
    content_type: str
    size: int

class DocumentListResponse(BaseModel):
    """Modelo para resposta com lista de documentos."""
    documents: List[DocumentResponse]
    total: int
    limit: int
    offset: int

router = APIRouter(
    prefix="/documents",
    tags=["documents"],
    responses={404: {"description": "Não encontrado"}}
)


@router.get("/")
async def get_documents():
    """
    Retorna a lista de todos os documentos
    """
    # Simulação inicial - em um caso real, você conectaria a um repositório
    return {"message": "Lista de documentos aqui (a ser implementada)"}

@router.post("/upload", response_model=DocumentResponse)
async def upload_document(file: UploadFile = File(...)):
    """
    Endpoint para fazer upload de um documento.
    Recebe um arquivo no formato docx/pdf ou outro e armazena no sistema
    
    Args:
        file: Arquivo a ser enviado (docx, pdf, etc)
        
    Returns:
        DocumentListResponse: Objeto contendo a lista atualizada de documentos após o upload
    """

    try:
        content = await file.read()

       

        print(f"Arquivo recebido: {file}")
        
        document = Document()

        document.name = file.filename
        document.file_type = file.content_type
        document.content = content

        # Aqui você implementaria a lógica para salvar o documento
        # Por enquanto, apenas simulamos um ID gerado
        document.id = str(uuid4())

        return DocumentResponse(
            id=document.id,
            name=document.name,
            file_type=document.file_type,
            size_kb=document.size_kb,
            chunks_count=document.chunks_count,
            processed=document.processed,
            message="Documento processado com sucesso"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao fazer upload: {str(e)}")


