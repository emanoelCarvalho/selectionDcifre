from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cnpj = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    obligations = relationship("AccessoryObligation", back_populates="company")

class AccessoryObligation(Base):
    __tablename__ = 'accessory_obligations'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    frequency = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship("Company", back_populates="obligations")