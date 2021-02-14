from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import routes


APP = FastAPI(
    title='Fortuna',
    description='Random Value Toolkit',
    version='0.1',
    docs_url='/',
)

APP.include_router(routes.router)

APP.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
