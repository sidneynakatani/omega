from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Login(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        user = request.form['user']
        password = request.form['pass']
        auth = False        

    
        if(user == 'sid' and password == 'cat'):
             auth = True 


        return {'auth': auth}


api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run(debug=True)

