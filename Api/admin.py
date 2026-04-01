from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Register
from .models import Search_data

admin.site.register(Search_data)
admin.site.register(Register,UserAdmin)

# Register your models here.
