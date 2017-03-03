from flask import request
from flask_restful import Resource
from model.credential import Credential


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
