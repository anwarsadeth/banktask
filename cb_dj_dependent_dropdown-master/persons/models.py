from django.db import models
from multiselectfield import MultiSelectField


class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Account_type(models.Model):
    name = models.CharField(max_length=40)


    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=124)
    age = models.IntegerField(default=None)
    dob = models.DateField()
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, blank=True, null=True)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=100)
    address = models.TextField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
    account_type = models.ForeignKey(Account_type, on_delete=models.SET_NULL, blank=True, null=True)

    MY_CHOICES2 = ((1, 'Passbook'),
                  (2, 'Chequebook'),
                  (3, 'Atm Card'),
                   (4, 'Credit Card'),

                  )

    documents_have = MultiSelectField(choices=MY_CHOICES2,max_choices=3)


    def __str__(self):
        return self.name
