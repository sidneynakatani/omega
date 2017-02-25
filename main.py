from flask          import Flask
from flask_restful  import Api
from api.login      import LoginApi
from api.register   import RegisterApi
from api.activate   import ActivateApi
from api.forgotPass import ForgotPassApi
from api.pet        import PetApi

app = Flask(__name__)
api = Api(app)


api.add_resource(LoginApi, '/login')
api.add_resource(RegisterApi, '/register')
api.add_resource(ActivateApi, '/activate')
api.add_resource(ForgotPassApi, '/forgotPass')
api.add_resource(PetApi, '/pet')

if __name__ == '__main__':
    app.run(debug=True)
    
