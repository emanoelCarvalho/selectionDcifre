from pydantic import BaseModel
from typing import Optional

class CompanyBase(BaseModel):
    name: str
    cnpj: str
    address: str
    email: str
    phone: str

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    cnpj: Optional[str] = None
    address: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

class Company(CompanyBase):
    id: int

    class Config:
        orm_mode = True

class AccessoryObligationBase(BaseModel):
    name: str
    frequency: str
    company_id: int

class AccessoryObligationCreate(AccessoryObligationBase):
    pass

class AccessoryObligationUpdate(BaseModel):
    name: Optional[str] = None
    frequency: Optional[str] = None
    company_id: Optional[int] = None

class AccessoryObligation(AccessoryObligationBase):
    id: int

    class Config:
        orm_mode = True