from db.connectionfactory import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from model.credential import Credential
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Pet(Base):

    __tablename__ = 'pet'
   
    id = Column(Integer, primary_key=True)
    pet_name = Column(String(50))
    pet_kind = Column(String(20))

    credential_id = Column(Integer, ForeignKey('credential.id'))
    credential = relationship("Credential")
   

    def __init__(self, pet_name, pet_kind, credential_id):

        self.pet_name = pet_name
	self.pet_kind = pet_kind
	self.credential_id = credential_id
