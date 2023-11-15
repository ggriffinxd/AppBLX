from fastapi import FastAPI,Request,BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.routers import produtosr, usuariosr, pedidor
from src.jobs.write_notification import write_notification

# banco de dados

app = FastAPI()

# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUT PRODUCTS

app.include_router(produtosr.router)


# ROUT AUTENTICATION AND SIGNUP

app.include_router(usuariosr.router)


# ROUT QUERY

app.include_router(pedidor.router)

#backgroundtaks
@app.post('/send_email/{email}')
def send_email(email: str, background: BackgroundTasks):
    background.add_task(write_notification,email,'Olá tudo bem?!')
    return {'OK': 'MSG ENVIADA'}

#Middleware


@app.middleware('http')
async def processarTempoRequisicao(request: Request,next):
    
    print("interceptou chegada")

    response = await next(request)

    print("interceptou a volta")

    return response