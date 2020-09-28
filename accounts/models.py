from django.db import models

# Create your models here.
class Register(models.Model):
    # FirstName = models.CharField(max_length=100)
    # MiddleName = models.CharField(max_length=100)
    # LastName = models.CharField(max_length=100)
    # UserName = models.CharField(max_length=50)
    EmailId = models.EmailField(max_length=50)
    # AadhaarRegisteredMobileNumber = models.BigIntegerField()
    # AadhaarNumber = models.BigIntegerField()
    Password = models.CharField(max_length=50)
    #ConfirmPassword = models.CharField(max_length=50)
    # AlternateMobileNumber = models.BigIntegerField()
    # Otp = models.BigAutoField()





    