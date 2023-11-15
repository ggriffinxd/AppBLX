from passlib.context import CryptContext

pwdcontext = CryptContext(schemes=['bcrypt'])

def verificar_hash(texto, hash):
    return pwdcontext.verify(texto,hash)

def gerar_hash(texto):
    return pwdcontext.hash(texto)