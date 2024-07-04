from django.contrib import admin

# Register your models here.
from .models import UserInfo,Experiencee

admin.site.register(UserInfo)
admin.site.register(Experiencee)