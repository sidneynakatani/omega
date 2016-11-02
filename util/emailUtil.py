import sendgrid 
import os 
from sendgrid.helpers.mail import * 

class EmailUtil():

	def send(self, email):
	     
             status = True             

             try:
	          print(email)	 
	          sg = sendgrid.SendGridAPIClient(apikey = os.getenv('SENDGRID_KEY'))
		  from_email = Email("test@example.com")
		  to_email = Email(email)
		  subject = "Sending with SendGrid is Fun"
		  content = Content("text/plain", "and easy to do anywhere, even with Python")
		  mail = Mail(from_email, subject, to_email, content)
		  response = sg.client.mail.send.post(request_body=mail.get())
		  print(response.status_code)

             except:
	          
                  print 'Falha ao enviar e-mail'
		  status = False

	     return status

