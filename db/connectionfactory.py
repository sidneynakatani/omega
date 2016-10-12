from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import QueuePool
import os

#user     = os.environ['USER']
#password = os.environ['PASS']
#host     = os.environ['HOST']
#port     = os.environ['PORT']
#database = os.environ['DATABASE']

#url = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format{user, password, host, port, database}
url = 'postgresql://indhzlkmaahykf:JQ58qiRbALZDmmR2jIMt1b0iRc@ec2-54-83-40-119.compute-1.amazonaws.com:5432/daf71h3n91rguu'

engine = create_engine(url, poolclass=QueuePool)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
                                       

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import model
    Base.metadata.create_all(bind=engine)

