from django.db import models

# Create your models here.
class donorform(models.Model):
    name = models.CharField(max_length=50,null= True,blank=True)
    email = models.EmailField(null= True,blank=True)
    contact_number = models.IntegerField(null= True,blank=True)
    age = models.IntegerField(null= True,blank=True)
    blood_group = models.CharField(max_length=20,null= True,blank=True)
    address = models.CharField(max_length=70,null= True,blank=True)


    def __str__(self):
        return self.name

class requesterlist(models.Model):
    patient_name = models.CharField(max_length=50, null=True, blank=True)
    contact_name = models.CharField(max_length=50, null=True, blank=True)
    doctor_name = models.CharField(max_length=50, null=True, blank=True)
    patient_address = models.CharField(max_length=90, null=True, blank=True)
    blood_group = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    mobile_number = models.IntegerField(null=True, blank=True)

