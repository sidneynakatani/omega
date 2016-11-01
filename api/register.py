import datetime 
import sendgrid 
import os 
from sendgrid.helpers.mail import * 
from db.connectionfactory import db_session
from model.credential import Credential
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
		 
		  credential = Credential(email, password, firstName, lastName, False, now)
                  db_session.add(credential)
		  db_session.commit()

		  sg = sendgrid.SendGridAPIClient(os.getenv('SENDGRID_KEY'))
		  from_email = Email("test@example.com")
		  to_email = Email("slack.hiroshi@gmail.com")
		  subject = "Sending with SendGrid is Fun"
		  content = Content("text/plain", "and easy to do anywhere, even with Python")
		  mail = Mail(from_email, subject, to_email, content)
		  response = sg.client.mail.send.post(request_body=mail.get())
		  print(response.status_code)

	     except:
	          
                  print 'Erro ao persistir'
		  status = False

	     return {'status': status}

	
