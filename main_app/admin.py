from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(UserInfo)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(ContactInfo)
