from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tên', {'fields': ['name']}),
        ('Quốc gia', {'fields': ['country']}),
    ]

admin.site.register(Customer, CustomerAdmin)