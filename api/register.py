import datetime 
from db.connectionfactory import db_session
from model.credential import Credential
from util.emailUtil import EmailUtil
from flask_restful import Resource
from flask import request

class RegisterApi(Resource):

	
	def get(self):
             email = EmailUtil()
             email.send('sidney.nakatani@hotmail.com')
	     return {'Api': 'Register'}

	def post(self):
		
	     status = True

	     try:
		 
	          email = request.form['email']
		  password = request.form['password']
		  firstName = request.form['firstName']
		  lastName = request.form['lastName']
                  now = datetime.datetime.now()
		 
		  credential = Credential(email, password, firstName, lastName, False, now)
                  db_session.add(credential)
		  db_session.commit()

                  print(email)
		  email = EmailUtil()
		  email.send(email)

	     except:
	          
                  print 'Erro ao persistir'
		  status = False

	     return {'status': status}

	
