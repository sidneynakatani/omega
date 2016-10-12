#from db.connectionfactory import Base, init_db, db_session
#from model.credential import Credential
#import datetime

#Test Postgree
#Create Tables
#init_db()

#Insert 
#now = datetime.datetime.now()
#credential = Credential('admin@admin.com.br', '123456', 'a', 'b', True, now)
#db_session.add(credential)
#db_session.commit()

#Select 
#a = Credential.query.filter_by(first_name='a', last_name='b').first()
#print a.last_name
#print a.password


#Test Mongodb

#key = Key(passKey='abcdef', createdAt=datetime.datetime.now())
#key.save();

#key = Key.query.filter(Key.passKey == 'abcdef').first()
#print key.createdAt


