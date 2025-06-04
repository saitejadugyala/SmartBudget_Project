from django.contrib import admin
from .models import CustomUser, Category, Transaction, Budget

# Register your models here.
admin.site.register(CustomUser)  # Assuming CustomUser is defined in models.py
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Budget)
# Register your models here.
