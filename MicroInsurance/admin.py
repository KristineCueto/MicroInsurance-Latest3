from django.contrib import admin
from django.contrib.auth.models import Group, User
from MicroInsurance.models import Branch, UnderWriter

admin.site.register(Branch)
admin.site.register(UnderWriter)
