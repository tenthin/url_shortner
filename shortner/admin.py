from django.contrib import admin
from .models import Url      #After creating model and migration in models.py, import in admin.py 
# Register your models here.
admin.site.register(Url)