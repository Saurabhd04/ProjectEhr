from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    Name = models.CharField(max_length=100)
    EmailId = models.EmailField(max_length=50)
    