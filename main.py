from flask         import Flask
from flask_restful import Api
from api.login     import LoginApi
from api.register  import RegisterApi
from api.activate  import ActivateApi

app = Flask(__name__)
api = Api(app)


api.add_resource(LoginApi, '/login')
api.add_resource(RegisterApi, '/register')
api.add_resource(ActivateApi, '/activate')

if __name__ == '__main__':
    app.run(debug=True)
    
