from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import tokenprovider
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from jose import JWTError

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

def obter_user_logado(token: str = Depends(oauth2_schema), session: Session = Depends(get_db)):
    
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='token inválido!')
    

    try:
      telefone = tokenprovider.verificarAcessToken(token)
    except JWTError:
       raise exception
    
    if not telefone:
       raise exception
   
    usuario = RepositorioUsuario(session).obterTelefone(telefone)

    if not usuario:
       raise exception
    
    return usuario