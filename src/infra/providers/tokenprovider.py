from datetime import datetime,timedelta
from jose import jwt

#CONFIG

SECRECT_KEY = 'caa9c8f8620cbb30679026bb6427e11f'
ALGORITHM = "HS256"
EXPIRES_IN_MIN = 3000
  
def criarAcessToken(data: dict):
    dados = data.copy()
   
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)
   
    dados.update({'exp': expiracao})

    tokenJwt = jwt.encode(dados,SECRECT_KEY,algorithm=ALGORITHM)
    return tokenJwt


def verificarAcessToken(token: str):
    carga = jwt.decode(token,SECRECT_KEY,algorithms=[ALGORITHM])
    return carga.get('sub')
