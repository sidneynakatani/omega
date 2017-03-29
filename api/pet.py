from flask_restful import Resource
from flask import request
from model.pet import Pet
from db.connectionfactory import db_session
import datetime

class PetApi(Resource):

     def get(self):
          return {'Api': 'Pet'}


     def post(self):
		
          created = True
          now = datetime.datetime.now()

	  try:
               
               userId = request.form['userId']
               imgId  = request.form['imgId']
               name   = request.form['name']
	       kind   = request.form['kind']
	       status = request.form['status']
               
	       address = request.form['address']
	       quarter = request.form['quarter']
	       city    = request.form['city']
	       state   = request.form['state']
	       country = request.form['country']
	       zipCode = request.form['zipCode']
               
               pet = Pet(name, kind, status, imgId, now,  userId)
 	       db_session.add(pet)
               db_session.flush()
               address = Address( address, quarter, city, state, zipCode, country, pet.id)
	      
	       db_session.add(address)
               db_session.commit()
		
		

          except:
	          
               print 'Erro ao persistir'
	       created = False

	  return {'status': created}




     def put(self):

          updated = False
	  
	  try:
               
               petId  = request.form['petId']
               name   = request.form['name']
	       kind   = request.form['kind']
	       status = request.form['status']
              
               
               pet = Pet.query.filter_by(id = petId).first()
 	       pet.pet_name = name
	       pet.pet_kind = kind
               pet.status = status
	       db_session.add(pet)
               db_session.flush()
               db_session.commit()
	       updated = True
		
          except:
	          
               print 'Erro ao atualizar'
	       updated = False

	  return {'status': updated}



