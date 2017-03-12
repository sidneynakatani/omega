from flask import request
from flask_restful import Resource
from model.credential import Credential
from db.connectionfactory import db_session
import datetime

class UserApi(Resource):

    def get(self):
        return {'Api': 'User'}


    def post(self):
        user_code = request.form['user_code']
        
	first_name = ''        
	last_name  = ''
	email      = ''

	
	try:
	    credential = Credential.query.filter_by(id = user_code).first()
            email      = credential.email
            first_name = credential.first_name
            last_name  = credential.last_name 


	except:

             print 'Nao foi possivel buscar dados.'
    
        
        return {'first_name': first_name, 'last_name' : last_name,  'email' : email}



    def put(self):
	status = True

	user_code  = request.form['user_code']
	first_name = request.form['first_name']
	last_name  = request.form['last_name']
	email      = request.form['email']
	password   = request.form['password']
	now = datetime.datetime.now()

	try:
	    credential = Credential.query.filter_by(id = user_code).first()
	    credential.first_name  = first_name
	    credential.last_name   = last_name
	    credential.update_date = now 

	    if self.isNotNone(email):
	        credential.email = email
	    
	    if self.isNotNone(password):
                credential.password = password
            
	    db_session.commit()

	except:
	     status = False
             print 'Nao foi possivel buscar dados.'
    
        
        return status



    def isNotNone(self, value):
        return value.strip() and value is not None


