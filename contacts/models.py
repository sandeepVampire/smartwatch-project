from django.db import models

# Create your models here.
class Contacts(models.Model):
    first_name = models.CharField(max_length=30,null = True, blank=True)
    middle_name = models.CharField(max_length=30,null = True, blank=True)
    last_name = models.CharField(max_length=30,null = True, blank=True)
    address = models.CharField(max_length=30,null = True, blank=True)
    phone = models.CharField(max_length=30,null = True, blank=True)
    mobile = models.CharField(max_length=30, null=True, blank=True)
    home = models.CharField(max_length=30, null=True, blank=True)
    email_id = models.CharField(max_length=30, null=True, blank=True)
    notes = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.first_name