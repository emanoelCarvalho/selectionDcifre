from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.AccessoryObligation)
def create_obligation(obligation: schemas.AccessoryObligationCreate, db: Session = Depends(get_db)):
    db_obligation = models.AccessoryObligation(**obligation.dict())
    db.add(db_obligation)
    db.commit()
    db.refresh(db_obligation)
    return db_obligation

@router.get("/{obligation_id}", response_model=schemas.AccessoryObligation)
def read_obligation(obligation_id: int, db: Session = Depends(get_db)):
    db_obligation = db.query(models.AccessoryObligation).filter(models.AccessoryObligation.id == obligation_id).first()
    if db_obligation is None:
        raise HTTPException(status_code=404, detail="Obligation not found")
    return db_obligation

@router.patch("/{obligation_id}", response_model=schemas.AccessoryObligation)
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

@router.delete("/{obligation_id}", response_model=schemas.AccessoryObligation)
def delete_obligation(obligation_id: int, db: Session = Depends(get_db)):
    db_obligation = db.query(models.AccessoryObligation).filter(models.AccessoryObligation.id == obligation_id).first()
    if db_obligation is None:
        raise HTTPException(status_code=404, detail="Obligation not found")

    db.delete(db_obligation)
    db.commit()
    return db_obligation
