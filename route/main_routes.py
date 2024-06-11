from fastapi import APIRouter, Form, Query, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from util.cookies import adicionar_cookie_mensagem

router = APIRouter()
templates = Jinja2Templates(directory="template")


@router.get("/")
async def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/entrar")
async def get_entrar(request: Request):
    return templates.TemplateResponse("entrar.html", {"request": request})


@router.post("/post_entrar")
async def post_entrar(request: Request, email: str = Form(...), senha: str = Form(...)):
    response = RedirectResponse("/", status_code=status.HTTP_302_FOUND)
    adicionar_cookie_mensagem(
        response, f"Entrada de usuário <b>{email}</b> realizada com sucesso!"
    )
    return response


@router.get("/cadastrar")
def get_cadastrar(request: Request):
    return templates.TemplateResponse("cadastrar.html", {"request": request})


@router.post("/post_cadastrar")
async def post_cadastrar(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    conf_senha: str = Form(...),
):
    response = RedirectResponse("/entrar", status_code=status.HTTP_302_FOUND)
    adicionar_cookie_mensagem(
        response,
        f"Usuário <b>{nome}</b> cadastrado com sucesso! Use suas credenciais para entrar.",
    )
    return response


@router.get("/produto/{id}")
def get_produto(request: Request, id: int):
    return templates.TemplateResponse("produto.html", {"request": request})


@router.get("/buscar")
def get_buscar(request: Request, q: str = Query(...)):
    return templates.TemplateResponse("buscar.html", {"request": request, "termo": q})
