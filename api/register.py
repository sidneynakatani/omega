import datetime
import hashlib 
from db.connectionfactory import db_session
from model.credential import Credential
from util.emailUtilV2 import EmailUtilV2
from flask_restful import Resource
from flask import request

import sendgrid
from sendgrid.helpers.mail import *

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

                  emailSender = EmailUtilV2()
                  sendEmail = str(email)
                  sendName  = str(firstName)
		  #emailSender.sendRegisterTemplate(sendEmail, sendName, hashApi)
                  self.sendEmail(sendEmail, sendName, hashApi)

	     except:
	          
                  print 'Erro ao persistir'
		  status = False

	     return {'status': status}


        def sendEmail(self, to, name, key):

             from_email = Email("sender@petsfinder.herokuapp.com")
	     subject = "[Petsfinder] Autenticar cadastro"
	     to_email = Email(to)
	     content = Content("text/html", " ")
	     mail = Mail(from_email, subject, to_email, content)
	     mail.personalizations[0].add_substitution(Substitution("-name-", name))
	     mail.personalizations[0].add_substitution(Substitution("-hashID-", key))
	     mail.set_template_id("e778cfa4-1b1b-472e-bd47-99db9a50a104")
             emailSender = EmailUtilV2()
             emailSender.send(mail)



              	
