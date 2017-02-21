#from db.connectionfactory import Base, init_db, db_session
#from model.credential import Credential
#from model.pet import Pet
#from model.address import Address
#import datetime

#Test Postgree
#Create Tables
#init_db()

#Insert Credential
#now = datetime.datetime.now()
#credential = Credential('admin@admin.com.br', '123456', 'a', 'b', True, now, '7d54ab1218bc7953fd56761c0d060989')
#db_session.add(credential)
#db_session.commit()

#Insert Pet
#pet = Pet('Batata', 'Gato','FOUNDED', '12wxe', now,  1)
#db_session.add(pet)
#db_session.commit()

#Insert Address
#address = Address( 'rua Teste 123', 'Bairro Teste', 'Santo Andre', 'SP', '0000000', 'Brasil', 1)
#db_session.add(address)
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


