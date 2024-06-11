from fastapi import APIRouter, File, Form, Request, UploadFile, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from util.cookies import adicionar_cookie_mensagem

router = APIRouter(prefix="/usuario")
templates = Jinja2Templates(directory="template")


@router.get("/gerenciamento")
def get_gerenciamento(request: Request):
    return templates.TemplateResponse("gerenciamento.html", {"request": request})


@router.get("/cadastrar_produto")
def get_cadastrar_produto(request: Request):
    return templates.TemplateResponse("cadastrar_produto.html", {"request": request})


@router.post("/post_cadastrar_produto")
async def post_cadastrar_produto(
    request: Request,
    nome: str = Form(...),
    descricao: str = Form(...),
    preco: float = Form(...),
    foto: UploadFile = File(...),
):
    response = RedirectResponse(
        "/usuario/gerenciamento", status_code=status.HTTP_302_FOUND
    )
    adicionar_cookie_mensagem(
        response, f"Produto <b>{nome}</b> cadastrado com sucesso!"
    )
    return response


@router.get("/alterar_produto/{id}")
def get_alterar_produto(request: Request, id: int):
    produto = {
        "id": id,
        "nome": "Produto de Teste",
        "descricao": "Descrição do produto.",
        "preco": 100.0,
    }
    return templates.TemplateResponse(
        "alterar_produto.html", {"request": request, "produto": produto}
    )


@router.post("/post_alterar_produto/{id}")
async def post_alterar_produto(
    request: Request,
    id: int,
    nome: str = Form(...),
    descricao: str = Form(...),
    preco: float = Form(...),
    foto: UploadFile = File(...),
):
    response = RedirectResponse(
        "/usuario/gerenciamento", status_code=status.HTTP_302_FOUND
    )
    adicionar_cookie_mensagem(response, f"Produto <b>{nome}</b> alterado com sucesso!")
    return response


@router.get("/excluir_produto/{id}")
def get_excluir_produto(request: Request, id: int):
    produto = {
        "id": id,
        "nome": "Produto de Teste",
        "descricao": "Descrição do produto.",
        "preco": 100.0,
    }
    return templates.TemplateResponse(
        "excluir_produto.html", {"request": request, "produto": produto}
    )


@router.post("/post_excluir_produto/{id}")
async def post_excluir_produto(request: Request, id: int, nome: str = Form(...)):
    response = RedirectResponse(
        "/usuario/gerenciamento", status_code=status.HTTP_302_FOUND
    )
    adicionar_cookie_mensagem(response, f"Produto <b>{nome}</b> excluído com sucesso!")
    return response


@router.get("/sair")
def get_sair(request: Request):
    response = RedirectResponse("/", status_code=status.HTTP_302_FOUND)
    return response
