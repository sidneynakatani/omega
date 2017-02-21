from db.connectionfactory import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from model.pet import Pet
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Address(Base):

    __tablename__ = 'address'
   
    id       = Column(Integer, primary_key=True)
    street   = Column(String(50))
    district = Column(String(20))
    city     = Column(String(20))
    state    = Column(String(2))
    zipcode  = Column(String(10))
    country  = Column(String(20))

    pet_id = Column(Integer, ForeignKey('pet.id'))
    pet = relationship("Pet")
   

    def __init__(self, street, district, city, state, zipcode, country, pet_id):

        self.street = street
	self.district = district
	self.city = city
	self.state = state
	self.zipcode = zipcode
	self.country = country
	self.pet_id = pet_id
