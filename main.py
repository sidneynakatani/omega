from flask          import Flask, request
from flask_restful  import Api
from api.login      import LoginApi
from api.register   import RegisterApi
from api.activate   import ActivateApi
from api.forgotPass import ForgotPassApi
from api.pet        import PetApi
from api.pets       import PetsApi
from api.user       import UserApi

app = Flask(__name__)
api = Api(app)

@app.before_request
def before_request():
     print request.args.get('user')


api.add_resource(LoginApi, '/login')
api.add_resource(RegisterApi, '/register')
api.add_resource(ActivateApi, '/activate')
api.add_resource(ForgotPassApi, '/forgotPass')
api.add_resource(PetApi, '/pet')
api.add_resource(PetsApi, '/pets')
api.add_resource(UserApi, '/user')

if __name__ == '__main__':
    app.run(debug=True)
    
