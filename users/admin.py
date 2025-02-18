from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# class CustomUserAdmin(UserAdmin):
#     model = User
#     # Define the fields to display in the list view
#     list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
#     list_filter = ('is_staff', 'is_active',)
#     ordering = ('email',)

admin.site.register(User)
