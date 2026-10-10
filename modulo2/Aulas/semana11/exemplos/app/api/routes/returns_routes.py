from fastapi import APIRouter
from fastapi.responses import JSONResponse, HTMLResponse, PlainTextResponse, RedirectResponse, FileResponse, StreamingResponse


router = APIRouter(prefix="/returns", tags=["Retornos"])

@router.get("json", summary="Retorna um JSON de exemplo", description="Retorna um JSON de exemplo com informações de teste")
def get_json():
    """
    Retorna um JSON de exemplo com informações de teste.
    """
    dados = {"message": "Este é um JSON de exemplo", "status": "success"}

    return JSONResponse(content=dados, status_code=200)

@router.get("/html", summary="Retorna um HTML de exemplo", description="Retorna um HTML de exemplo com informações de teste")
def get_html():
    """
    Retorna um HTML de exemplo com informações de teste.
    """
    html_content = """
    <html>
        <head>
            <title>Exemplo de HTML</title>
        </head>
        <body>
            <h1>Este é um HTML de exemplo</h1>
            <p>Status: success</p>
        </body>
    </html>
    """

    return HTMLResponse(content=html_content, status_code=200)

@router.get("/plaintext", summary="Retorna um texto simples de exemplo", description="Retorna um texto simples de exemplo com informações de teste")
def get_plaintext():
    """
    Retorna um texto simples de exemplo com informações de teste.
    """
    my_text="Este é um texto simples de exemplo\neste teste é puramente string, sem formatação HTML ou JSON."
    return PlainTextResponse(content=my_text, status_code=200)

@router.get("/redirect", summary="Redireciona para outra URL", description="Redireciona para outra URL de exemplo")
def redirect():
    """
    Redireciona para outra URL de exemplo.
    """
    return RedirectResponse(url="/games/list", status_code=302)

@router.get("/file", summary="Retorna um arquivo de exemplo", description="Retorna um arquivo de exemplo para download")
def get_file():
    """
    Retorna um arquivo de exemplo para download.
    """
    file_path = "app/api/routes/fiesc.jpg"  # Caminho para o arquivo de exemplo
    # return FileResponse(path=file_path, filename="fiesc.jpg", media_type="image/jpeg", headers={"Content-Disposition": "attachment; filename=fiesc.jpg"})
    return FileResponse(path=file_path, filename="fiesc.jpg", media_type="image/jpeg", headers={"Content-Disposition": "inline; filename=fiesc.jpg"})

import time
def gerador_relatorio():
    """
    Função geradora que simula a geração de um relatório em partes.
    """
    yield "Parte 1 do relatório\n"
    time.sleep(2)  # Simula um atraso na geração do relatório
    yield "Parte 2 do relatório\n"
    time.sleep(2)  # Simula um atraso na geração do relatório
    yield "Parte 3 do relatório\n"

@router.get("/stream", summary="Retorna um arquivo de exemplo como stream", description="Retorna um arquivo de exemplo como stream para download")
def get_file_stream():
    """
    Retorna um arquivo de exemplo como stream para download.
    """
    return StreamingResponse(gerador_relatorio(), media_type="text/plain")