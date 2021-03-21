from django.contrib import admin
from .models import Hospitals, Patient, State
# Register your models here.

admin.site.register(Hospitals)


admin.site.register(Patient)

admin.site.register(State)

