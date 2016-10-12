from flask import Flask, request
from flask_restful import Resource, Api
from model.credential import Credential


app = Flask(__name__)
api = Api(app)

class Login(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        email = request.form['email']
        password = request.form['pass']
        auth = False        

	try:
	     credential = Credential.query.filter_by(email = email, password = password).first()
             auth = credential.active

	except:
	     auth = False
    
        
        return {'auth': auth}


api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run(debug=True)
     

