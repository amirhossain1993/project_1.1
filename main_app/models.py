from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='user_info_images/')
    
    
class Experiencee(models.Model):
    passsing_year = models.CharField(max_length=300)
    skill = models.CharField(max_length=300)
    address = models.CharField(max_length=400)
    details = models.TextField()
    
    class Meta:
        verbose_name_plural ='Experience'
    

    def __str__(self):
        return self.passsing_year


