from .models import student
import time
from django.core.mail import send_mail
from django.conf import  settings

def run_this_function() :
    print("Function Started")
    time.sleep(1)
    print("Function Executed")

# to send a mail
def send_email_to_client():
    subject="This email is from Django server"
    message="This is working fine- Django server mail"
    from_email= settings.EMAIL_HOST_USER
    recipient_list=["nageshnaik.07081997@gmail.com"]
    send_mail(subject,message,from_email, recipient_list)
