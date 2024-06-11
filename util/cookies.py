from fastapi import Response


def adicionar_cookie_mensagem(response: Response, mensagem: str):
    response.set_cookie(
        key="mensagem",
        value=mensagem,
        max_age=1,
        httponly=True,
        samesite="lax",
    )
