import sendgrid
import os
from sendgrid.helpers.mail import *

class EmailUtilV2():

        def send(self, mail):

             status = True
             sg = sendgrid.SendGridAPIClient(apikey = os.getenv('SENDGRID_KEY'))
             
             try:
	          response = sg.client.mail.send.post(request_body=mail.get())
                  print(response.status_code)
                  
	     except urllib.HTTPError as e:
	          print e.read()
                  print(response.status_code)
                  status = False
	      
             return status
	
	
