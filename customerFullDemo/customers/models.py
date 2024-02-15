from django.db import models

class Customers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)
