from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal, engine
from fastapi.encoders import jsonable_encoder

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/companies/", response_model=schemas.Company)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    db_company = models.Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

@app.get("/companies/{company_id}", response_model=schemas.Company)
def read_company(company_id: int, db: Session = Depends(get_db)):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company

@app.patch("/companies/{company_id}", response_model=schemas.Company)
def update_company(company_id: int, company: schemas.CompanyUpdate, db: Session = Depends(get_db)):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    
    company_data = company.dict(exclude_unset=True)
    for key, value in company_data.items():
        setattr(db_company, key, value)
    
    db.commit()
    db.refresh(db_company)
    return db_company

@app.delete("/companies/{company_id}", response_model=schemas.Company)
def delete_company(company_id: int, db: Session = Depends(get_db)):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    
    db.delete(db_company)
    db.commit()
    return db_company

@app.post("/obligations/", response_model=schemas.AccessoryObligation)
def create_obligation(obligation: schemas.AccessoryObligationCreate, db: Session = Depends(get_db)):
    db_obligation = models.AccessoryObligation(**obligation.dict())
    db.add(db_obligation)
    db.commit()
    db.refresh(db_obligation)
    return db_obligation

@app.get("/obligations/{obligation_id}", response_model=schemas.AccessoryObligation)
def read_obligation(obligation_id: int, db: Session = Depends(get_db)):
    db_obligation = db.query(models.AccessoryObligation).filter(models.AccessoryObligation.id == obligation_id).first()
    if db_obligation is None:
        raise HTTPException(status_code=404, detail="Obligation not found")
    return db_obligation

@app.patch("/obligations/{obligation_id}", response_model=schemas.AccessoryObligation)
def update_obligation(obligation_id: int, obligation: schemas.AccessoryObligationUpdate, db: Session = Depends(get_db)):
    db_obligation = db.query(models.AccessoryObligation).filter(models.AccessoryObligation.id == obligation_id).first()
    if db_obligation is None:
        raise HTTPException(status_code=404, detail="Obligation not found")
    
    obligation_data = obligation.dict(exclude_unset=True)
    for key, value in obligation_data.items():
        setattr(db_obligation, key, value)
    
    db.commit()
    db.refresh(db_obligation)
    return db_obligation

@app.delete("/obligations/{obligation_id}", response_model=schemas.AccessoryObligation)
def delete_obligation(obligation_id: int, db: Session = Depends(get_db)):
    db_obligation = db.query(models.AccessoryObligation).filter(models.AccessoryObligation.id == obligation_id).first()
    if db_obligation is None:
        raise HTTPException(status_code=404, detail="Obligation not found")
    
    db.delete(db_obligation)
    db.commit()
    return db_obligation