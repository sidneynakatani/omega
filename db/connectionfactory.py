from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import QueuePool
import os


url = 'postgresql://{0}:{1}@{2}:5432/{3}'.format(os.getenv('USER'), os.getenv('PASS'), os.getenv('HOST'), os.getenv('DATABASE'))

engine = create_engine(url, poolclass=QueuePool)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
                                       

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import model
    Base.metadata.create_all(bind=engine)

