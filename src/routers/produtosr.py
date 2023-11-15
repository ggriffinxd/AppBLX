from fastapi import APIRouter, status, Depends, HTTPException
from src.schemas.schemas import Produto
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto

router = APIRouter()


@router.post("/produtos", status_code=201)
def criarProduto(produto: Produto, db: Session = Depends(get_db)):
    produtoCriado = RepositorioProduto(db).criar(produto)
    return {produtoCriado}


@router.put("/produtos/{id}", status_code=status.HTTP_201_CREATED)
def atualizarProduto(id: int, produtos: Produto, session: Session = Depends(get_db)):
    RepositorioProduto(session).upgrade(id, produtos)
    return {"produto_atualizado"}


@router.get("/produtos", status_code=status.HTTP_200_OK, response_model=list[Produto])
def listarProdutos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos


@router.delete("/produtos/{id}", status_code=status.HTTP_200_OK)
def listarProdutos(id: int, db: Session = Depends(get_db)):
    RepositorioProduto(db).remover(id)
    return {"Produto removido com sucesso!"}


@router.get("/produtos/{id}")
def exibirProdutos(id: int, session: Session = Depends(get_db)):
    produtoLocalizado = RepositorioProduto(session).exibirProduto(id)
    if not produtoLocalizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Produto não localizado com esse ID = {id}!"
        )
    return produtoLocalizado
