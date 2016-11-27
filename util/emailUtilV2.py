import sendgrid
import os
from sendgrid.helpers.mail import *

class EmailUtilV2():

        def send(self, email, name, hashApi):

             status = True
	     print email
	     print name
             print hashApi
             sg = sendgrid.SendGridAPIClient(apikey = os.getenv('SENDGRID_KEY'))
             from_email = Email("sender@petsfinder.herokuapp.com")
	     subject = "[Petsfinder] Autenticar cadastro"
	     to_email = Email(email)
	     content = Content("text/html", " ")
	     mail = Mail(from_email, subject, to_email, content)
	     mail.personalizations[0].add_substitution(Substitution("-name-", name))
	     mail.personalizations[0].add_substitution(Substitution("-hashID-", hashApi))
	     mail.set_template_id("e778cfa4-1b1b-472e-bd47-99db9a50a104")
	
             try:
	          response = sg.client.mail.send.post(request_body=mail.get())
                  print(response.status_code)
                  
	     except urllib.HTTPError as e:
	          print e.read()
                  print(response.status_code)
                  status = False
	    
	     return status
	
	
