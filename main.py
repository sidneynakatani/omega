from flask import Flask, request
from flask_restful import Resource, Api
from model.credential import Credential
from api.register import RegisterApi


app = Flask(__name__)
api = Api(app)


class Login(Resource):

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



api.add_resource(Login, '/login')
api.add_resource(RegisterApi, '/register', resource_class_kwargs={'request': request})

if __name__ == '__main__':
    app.run(debug=True)
    
     

