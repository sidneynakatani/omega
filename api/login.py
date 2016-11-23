from flask import request
from flask_restful import Resource
from model.credential import Credential


class LoginApi(Resource):

    def get(self):
        return {'Api': 'Login'}

    def post(self):
        email = request.form['email']
        password = request.form['pass']
        auth = False
        name = ''        
	
	try:
	    credential = Credential.query.filter_by(email = email, password = password).first()
            auth = credential.active
            name = credential.first_name

	except:
	     auth = False
             print 'Nao foi possivel autenticar.'
    
        
        return {'auth': auth, 'name' : name}
