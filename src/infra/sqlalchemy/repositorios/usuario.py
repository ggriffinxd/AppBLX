from sqlalchemy.orm import Session
from sqlalchemy import select
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioUsuario():
    def __init__(self, session: Session):
        self.session = session

    def criar(self, usuario: schemas.User):
        usuario_bd = models.Usuario(
            nome=usuario.nome, senha=usuario.senha, telefone=usuario.telefone
        )
        self.session.add(usuario_bd)
        self.session.commit()
        self.session.refresh(usuario_bd)
        return usuario_bd

    def listar(self):
        stmt = select(models.Usuario)
        usuarios = self.session.execute(stmt).scalars().all()
        return usuarios

    def obterTelefone(self, telefone):
        query = select(models.Usuario).where(models.Usuario.telefone == telefone)
        return self.session.execute(query).scalars().first()

    def remover():
        pass
