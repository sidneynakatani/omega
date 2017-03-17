from db.connectionfactory import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from model.credential import Credential
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Pet(Base):

    __tablename__ = 'pet'
   
    id           = Column(Integer, primary_key=True)
    pet_name     = Column(String(50))
    pet_kind     = Column(String(20))
    status       = Column(String(10))
    image_id     = Column(String(50))
    created_date = Column(DateTime())

    credential_id = Column(Integer, ForeignKey('credential.id'))
    credential = relationship("Credential")
   

    def __init__(self, pet_name, pet_kind, status, image_id, created_date, credential_id):

        self.pet_name      = pet_name
	self.pet_kind      = pet_kind
	self.status        = status
	self.image_id      = image_id
	self.created_date  = created_date
	self.credential_id = credential_id
