from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField( max_length=20)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null = True)
    


