from http.client import ImproperConnectionState
from django.contrib import admin
from .models import MyDetails

# Register your models here.
admin.site.register(MyDetails)