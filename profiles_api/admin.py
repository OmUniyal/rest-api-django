from django.contrib import admin

# Register your models here.

from django.contrib import admin
from profiles_api import models


admin.site.register(models.UserProfile)