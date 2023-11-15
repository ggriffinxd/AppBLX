from fastapi import APIRouter, Depends, status,HTTPException
from sqlalchemy.orm import Session
from src.schemas.schemas import User,LoginData,SimpleUser,LoginSucesso
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import hashprovider,tokenprovider
from src.routers.utils import obter_user_logado

router = APIRouter()


@router.post("/usuarios", status_code=status.HTTP_201_CREATED)
def criarUsuario(usuario: User, session: Session = Depends(get_db)):
    #verify
    usuariolocalizado = RepositorioUsuario(session).obterTelefone(usuario.telefone)

    if usuariolocalizado:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail= 'ja existe um user com esse telefone')

    #create
    usuario.senha = hashprovider.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@router.post("/token",response_model=LoginSucesso)
def login(loginData:LoginData, session: Session = Depends(get_db)):
    senha = loginData.senha
    telefone = loginData.telefone

    usuario = RepositorioUsuario(session).obterTelefone(telefone)
    
    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="telefone ou senha estão incorretas")
    
    senhaValida = hashprovider.verificar_hash(senha,usuario.senha)

    if not senhaValida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="telefone ou senha estão incorretas")
    token = tokenprovider.criarAcessToken({'sub': usuario.telefone})
    return LoginSucesso(usuario =usuario, acess_token= token)

@router.get('/me', response_model=SimpleUser)
def me(usuario: User = Depends(obter_user_logado), session: Session = Depends(get_db)):
    return usuario