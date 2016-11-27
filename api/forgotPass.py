import datetime
import hashlib 
from flask_restful import Resource
from flask import request
from model.credential import Credential
from db.connectionfactory import db_session

class ForgotPassApi(Resource):

     def get(self):
          return {'Api': 'ForgotPass'}


     def post(self):
		
          status = True

	  try:

	       #1 Adicionar um chave no Heroku para aumentar a segurança do hash
               email = request.form['email']
               now = datetime.datetime.now()
	       hashStr = str(now) + str(email)
               hashApi = hashlib.sha1(hashStr).hexdigest()
           
               credential = Credential.query.filter_by(email = email).first()
	       credential.hash_key = hashApi
               db_session.commit()
		
	       #2 Alterar EmailUtilV2 para envio de email generico


          except:
	          
               print 'Erro ao persistir'
	       status = False

	  return {'status': status}
