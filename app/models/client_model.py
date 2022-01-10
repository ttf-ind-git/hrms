from django.db import models
from django.contrib.auth.models import User 
from django.contrib.auth.models import Group

# Create your models here.

class Client(models.Model):  
    id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=30 , blank = False, null = False)
    first_name = models.CharField(max_length=30 , blank = False, null = False)
    last_name = models.CharField(max_length=30, blank = False, null = False)  
    email_id = models.EmailField(max_length=50, blank = False, null = False)  
    mobile_number = models.CharField(max_length=12, blank = False, null = False) 
    phone = models.CharField(max_length=12, blank = True, null = True) 
    fax = models.CharField(max_length=12, blank = True, null = True) 
    address = models.TextField (blank = True, null = True)  
    city = models.CharField(max_length=30, blank = True, null = True)  
    state = models.CharField(max_length=30, blank = True, null = True)  
    country = models.CharField(max_length=30, blank = True, null = True)  
    pincode = models.CharField(max_length=12, blank = True, null = True) 
    industry = models.CharField(max_length=50, blank = True, null = True)  
    company_size = models.CharField(max_length=20, blank = True, null = True)  
    description = models.TextField (blank = True, null = True)  
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    is_active = models.PositiveSmallIntegerField(default=1)
      
    class Meta:  
        db_table = "client"  

