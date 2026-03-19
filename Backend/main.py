# src/main.py
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from contextlib import asynccontextmanager
# from sqlmodel import SQLModel

# from core.config import settings
# from db.connection import engine
# from api import auth, todos
# from models import *

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     SQLModel.metadata.create_all(engine, checkfirst=True)
#     print("[OK] Database tables created")
#     yield

# app = FastAPI(
#     title="Evolution of Todo API",
#     description="Phase II Full-Stack Todo Web Application API",
#     version="1.0.0",
#     lifespan=lifespan,
# )

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
        
#         "http://localhost:3000",
#         "http://127.0.0.1:3000",
#         settings.frontend_url,
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(auth.router, tags=["auth"])
# app.include_router(todos.router, prefix="/api/v1", tags=["todos"])

# @app.get("/health")
# async def health_check():
#     return {"status": "healthy"}

# @app.get("/")
# async def root():
#     return {
#         "name": "Evolution of Todo API",
#         "version": "1.0.0",
#         "docs": "/docs",
#     }



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from sqlmodel import SQLModel

# Correct absolute imports from src
from src.core.config import settings


from src.db.connection import engine
from src.api import auth, todos
from src.models import *

# Lifespan context to create tables on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine, checkfirst=True)
    print("[OK] Database tables created")
    yield

# Create FastAPI app
app = FastAPI(
    title="Evolutionsiii of Todo API",
    description="Phase II Full-Stack Todo Web Application API",
    version="1.0.0",
    lifespan=lifespan,
)
print ("hello world")
# CORS Middleware (allow only your local frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:3000",
    "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(auth.router, tags=["auth"])
app.include_router(todos.router, prefix="/api/v1", tags=["todos"])

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Root endpoint
@app.get("/")
async def root():
    return {
        "name": "Evolution of Todo API",
        "version": "1.0.0",
        "docs": "/docs",
    }





