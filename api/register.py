import datetime
import hashlib 
from db.connectionfactory import db_session
from model.credential import Credential
from util.emailUtil import EmailUtil
from flask_restful import Resource
from flask import request

class RegisterApi(Resource):

	
	def get(self):
             return {'Api': 'Register'}

	def post(self):
		
	     status = True

	     try:
		 
	          email = request.form['email']
		  password = request.form['password']
		  firstName = request.form['firstName']
		  lastName = request.form['lastName']
                  now = datetime.datetime.now()
		  hashStr = str(now) + str(email)
                  hashApi = hashlib.sha1(hashStr).hexdigest()

		 
		  credential = Credential(email, password, firstName, lastName, False, now, hashApi)
                  db_session.add(credential)
		  db_session.commit()

                  sendEmail = str(email)
		  email = EmailUtil()
		  email.send(sendEmail)

	     except:
	          
                  print 'Erro ao persistir'
		  status = False

	     return {'status': status}

	
