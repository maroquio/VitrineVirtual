# main.py na raiz do projeto
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from route.main_routes import router as main_router
from route.usuario_routes import router as usuario_router

# criação do objeto que representa a aplicação web
app = FastAPI()
# montagem do diretório de arquivos estáticos (css, js, imagens etc.)
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
# adição dos módulos de rotas
app.include_router(main_router)
app.include_router(usuario_router)
# execução do servidor web
if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True)
