from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='user_info_images/')
    
    
