import sendgrid
import os
from sendgrid.helpers.mail import *

class EmailUtilV2():

        def send(self, email, name, hashApi):

             status = True

             try:
                  
                  sg = sendgrid.SendGridAPIClient(apikey = os.getenv('SENDGRID_KEY'))
                  
                  data = {
 		     		"to": "sidney.nakatani@hotmail.com",
  		     		"sub": { "-name-": "Sidney", "-hashID-": "5678" }, 
  		     		"template_id": "e778cfa4-1b1b-472e-bd47-99db9a50a104"
                 	 }

		  template_id = "e778cfa4-1b1b-472e-bd47-99db9a50a104"
		  response = sg.client.templates._(template_id).versions.post(request_body=data)
		  print(response.status_code)
		  print(response.body)
		  print(response.headers)

             except:

                  print 'Falha ao enviar e-mail'
                  status = False

             return status

