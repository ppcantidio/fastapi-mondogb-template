from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ${{ values.module }}.routers.v1 import user_router


def app_v1(app: FastAPI):
    app.include_router(user_router.router, prefix="/v1")


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app_v1(app)
