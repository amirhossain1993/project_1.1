from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='user_info_images/')
    
    
class Experience(models.Model):
    passsing_year = models.CharField(max_length=300)
    skill = models.CharField(max_length=300)
    address = models.CharField(max_length=400)
    details = models.TextField()
    
    class Meta:
        verbose_name_plural ='Experience'
    

    def __str__(self):
        return self.passsing_year


class Education(models.Model):
    passsing_year = models.CharField(max_length=300)
    univercity_name = models.CharField(max_length=300)
    depertment = models.CharField(max_length=400)
    details = models.TextField()
    
    class Meta:
        verbose_name_plural ='Education'
    

    def __str__(self):
        return self.passsing_year
    
    
    
    
    
class ContactInfo(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone_number = models.CharField(max_length=400)
    message = models.TextField()
    
    class Meta:
        verbose_name_plural ='ContactInfo'
    

    def __str__(self):
        return self.name
    
    
    
    
    


    

