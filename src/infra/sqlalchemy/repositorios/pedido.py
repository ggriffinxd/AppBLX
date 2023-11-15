from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import List
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioPedido():
    def __init__(self, session: Session):
        self.session = session

    def gravarPedido(self, pedido: schemas.Pedidos) -> models.Pedido:
        db_pedido = models.Pedido(
            quantidade=pedido.quantidade,
            localDeEntrega=pedido.localDeEntrega,
            tipoDeEntrega=pedido.tipoDeEntrega,
            observacao=pedido.observacao,
            usuario_id=pedido.usuario_id,
            produto_id=pedido.produto_id,
        )
        self.session.add(db_pedido)
        self.session.commit()
        self.session.refresh(db_pedido)

        return db_pedido

    def buscarPedido(self, id: int) -> models.Pedido:
        query = select(models.Pedido).where(models.Pedido.id == id)
        pedido = self.session.execute(query).scalars().all()
        
        return pedido
        #return pedido[0]
    
    def listarMeusPedidosPorUsuarioId(self, usuario_id: int):
        query = select(models.Pedido).where(models.Pedido.usuario_id == usuario_id)
        pedido = self.session.execute(query).scalars().all()
        
        return pedido

    def listarMinhasVendasPorUsuarioId(self, usuario_id: int):
        query = select(models.Pedido,models.Produto) \
        .join_from(models.Pedido,models.Produto) \
        .where(models.Pedido.usuario_id == usuario_id)
        
        pedido = self.session.execute(query).scalars().all()
        
        return pedido
