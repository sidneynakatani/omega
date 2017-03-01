from flask_restful import Resource
from flask import request
from model.pet import Pet
from db.connectionfactory import db_session
from flask import jsonify

class PetsApi(Resource):

     def get(self):
          return {'Api': 'Pets'}


     def post(self):
	
       
        user_code = request.form['user_code']
              
	try:
	   
            result = db_session.query(Pet.id, Pet.pet_name, Pet.created_date, Pet.pet_kind, Pet.status).filter_by(credential_id = user_code).all()
         
        except:	          
            print 'Erro ao executar a busca.'

        return jsonify(pets=result)
