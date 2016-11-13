from db.connectionfactory import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

class Credential(Base):

    __tablename__ = 'credential'

    id = Column(Integer, primary_key=True)
    email = Column(String(60), unique=True)
    password = Column(String(30))
    first_name = Column(String(50))
    last_name = Column(String(50))
    active = Column(Boolean())
    update_date = Column(DateTime())
    hash_key = Column(String(50))

    def __init__(self, email, password, first_name, last_name, active, update_date, hash_key):

        self.email = email
        self.password = password
        self.first_name = first_name
	self.last_name = last_name
        self.active = active
        self.update_date = update_date
        self.hash_key = hash_key

    
    def is_authenticated(self):
        return True

 
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


    def __repr__(self):
        return '<Credential %r>' % (self.first_name)
