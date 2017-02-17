import datetime
import hashlib 
from flask_restful import Resource
from flask import request
from model.credential import Credential
from db.connectionfactory import db_session
from util.emailUtilV2 import EmailUtilV2
import sendgrid
from sendgrid.helpers.mail import *

class ForgotPassApi(Resource):

     def get(self):
          return {'Api': 'ForgotPass'}


     def post(self):
		
          status = True

	  try:
               
               email = request.form['email']
               now = datetime.datetime.now()
	       hashStr = str(now) + str(email)
               hashApi = hashlib.sha1(hashStr).hexdigest()
           
               credential = Credential.query.filter_by(email = email).first()
	       credential.hash_key = hashApi
               db_session.commit()

               name = credential.first_name
	       self.sendEmail(email, name, hashApi)
               
          except:
	          
               print 'Erro ao enviar email'
	       status = False

	  return {'status': status}


     def put(self):
          
          email = ''
          name  = ''
          status = True

          try:

               receivedPass = request.form['password']
	       receivedHash = request.form['hash']
               
	       credential = Credential.query.filter_by(hash_key = receivedHash).first()
               email =  credential.email
               name  =  credential.first_name 
	       now = datetime.datetime.now()
	       hashStr = str(now) + str(email)
               hashApi = hashlib.sha1(hashStr).hexdigest()
               
               credential.hash_key = hashApi
               credential.password = receivedPass
               db_session.commit()
               
	       
	  except:

	       print 'Erro ao atualizar registro'
               status = False

	  return {'updated': status, 'name': name}


     	


     def sendEmail(self, to, name, key):
          
          from_email = Email("sender@petsfinder.herokuapp.com")
	  subject = "[Petsfinder] Pedido para alterar senha"
	  to_email = Email(to)
	  content = Content("text/html", " ")
	  mail = Mail(from_email, subject, to_email, content)
	  mail.personalizations[0].add_substitution(Substitution("-name-", name))
	  mail.personalizations[0].add_substitution(Substitution("-hashID-", key))
	  mail.set_template_id("1ba9c30f-b867-4e51-82c3-857a6fb02be5")
          emailSender = EmailUtilV2()
          emailSender.send(mail)
             


