from fastapi import FastAPI
import models
from database import engine
import companies
import obligations

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(companies.router, prefix="/companies", tags=["companies"])
app.include_router(obligations.router, prefix="/obligations", tags=["obligations"])
