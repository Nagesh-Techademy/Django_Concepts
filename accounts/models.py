# from django.db import models
#
# # Create your models here.
# from django.contrib.auth.models import  AbstractUser
#
# class CustomUser(AbstractUser):
#     username=None
#     phone_number= models.CharField(max_length=100,unique=True)
#     email= models.EmailField(unique=True)
#     user_bio= models.CharField(max_length=50)
#     user_profile_image=models.ImageField(uploaad_to="profile")
#
#     USERNAME_FIELD = 'phone_number'  # If you add this field then you can login with thisfield like phone no.
#     REQUIRED_FIELDS = []

    # need to write a model manager
    #When you call python manage.py createsuperuser that time it will take only email username and password but in this case we
    #have provided multiple parameter so we need to write
    #manager (Check manager.py)


# Need to add AUTH_USER_MODEL='accounts.CustomUser' in setting.py to tell it is a custom module