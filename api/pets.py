from flask_restful import Resource
from flask import request
from model.pet import Pet
from model.address import Address
from db.connectionfactory import db_session
from flask import jsonify

class PetsApi(Resource):

     def get(self):
          return {'Api': 'Pets'}


     def post(self):
	
       
        user_code = request.form['user_code']
              
	try:
	   
	    result = db_session.query(Pet.id, Pet.pet_name, Pet.created_date, Pet.pet_kind, Pet.status, Pet.image_id, Address.city, Address.street, Address.country).filter_by(credential_id = user_code).filter(Pet.id == Address.pet_id).all()
         
        except:	          
            print 'Erro ao executar a busca.'

        return jsonify(pets=result)
