from pydantic import BaseModel

class CompanyBase(BaseModel):
    name: str
    cnpj: str
    address: str
    email: str
    phone: str

class CompanyCreate(CompanyBase):
    pass

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

class AccessoryObligation(AccessoryObligationBase):
    id: int

    class Config:
        orm_mode = True