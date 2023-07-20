from django.db import models

# Create your models here.
class Registration(models.Model):
    user_pic = models.ImageField(upload_to='User/Porfile/%Y/%m/%d',null=True ,blank=True)
    first_name =models.CharField(max_length=50 )
    last_name =models.CharField(max_length=50)
    email =models.EmailField(max_length=150)
    password =models.CharField(max_length=150)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    