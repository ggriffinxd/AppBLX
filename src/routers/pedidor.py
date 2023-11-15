from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.routers.utils import obter_user_logado
from src.infra.sqlalchemy.repositorios.pedido import RepositorioPedido
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Pedidos,User
router = APIRouter()


@router.post("/pedidos", status_code=status.HTTP_201_CREATED)
def fazerPedido(pedido: Pedidos, session: Session = Depends(get_db)):
    pedidoCriado = RepositorioPedido(session).gravarPedido(pedido)
    return pedidoCriado


@router.get("/pedidos/{id}")
def exibirPedido(id: int, session: Session = Depends(get_db)):
    try:
        acharPedido = RepositorioPedido(session).buscarPedido(id)
        return acharPedido
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Produto não existe com id = {id}")


@router.get("/pedidos",response_model=list[Pedidos])
def listarPedidos(userId: User = Depends(obter_user_logado), session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(session).listarMeusPedidosPorUsuarioId(userId.id)
    return pedidos


@router.get("/pedidos/{id}/vendas")
def listarVendas(id: int, session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(session).listarMinhasVendasPorUsuarioId(id)
    return pedidos
