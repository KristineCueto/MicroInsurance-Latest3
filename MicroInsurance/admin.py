from django.contrib import admin
from django.contrib.auth.models import Group, User
from MicroInsurance.models import Branch, UnderWriter, Insurance, Promo, UserType

admin.site.register(Branch)
admin.site.register(UnderWriter)
admin.site.register(Insurance)
admin.site.register(Promo)
admin.site.register(UserType)
admin.site.disable_action('delete_selected')
