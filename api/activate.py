from flask_restful import Resource
from flask import request
from model.credential import Credential
from db.connectionfactory import db_session

class ActivateApi(Resource):

     def get(self):
          return {'Api': 'Activate'}


     def post(self):
		
          status = True

	  try:

               hashId = request.form['hashId']
               credential = Credential.query.filter_by(hash_key = hashId).first()
	       credential.active = True
               db_session.commit()
		
		

          except:
	          
               print 'Erro ao persistir'
	       status = False

	  return {'status': status}
