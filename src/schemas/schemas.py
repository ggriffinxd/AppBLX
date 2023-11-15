from pydantic import BaseModel
from typing import List


class ProdutoSimples(BaseModel):
    id: int | None = None
    nome: str
    preco: float

    class Config:
        from_attributes = True


class User(BaseModel):
    id: int | None = None
    nome: str
    telefone: str
    senha: str
    produtos: List[ProdutoSimples] = []

    class Config:
        from_attributes = True


class SimpleUser(BaseModel):
    nome: str
    telefone: str

    class Config:
        from_attributes = True

class LoginData(BaseModel):
    senha: str
    telefone: str

class LoginSucesso(BaseModel):
    usuario: SimpleUser
    acess_token: str


class Produto(BaseModel):
    id: int | None = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: int | None = None
    usuario: SimpleUser | None = None

    class Config:
        from_attributes = True


class Pedidos(BaseModel):
    id: int | None = None
    quantidade: int
    localDeEntrega: str | None = None
    tipoDeEntrega: str
    observacao: str | None = None

    usuario_id: int | None = None
    produto_id: int | None = None

    usuario: SimpleUser | None = None
    produto: Produto | None = None

    class Config:
        from_attributes = True
