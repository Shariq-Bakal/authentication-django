from django.contrib import admin

# this will show users in the admin

from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    list_display = ["id","email", "name", "role", "date_of_birth", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name","date_of_birth","role"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    #fieldsets is used to organize fields into sections when editing an existing record in the admin panel. It groups related fields together, making the form more user-friendly and easier to navigate.
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email","name", "role" "date_of_birth", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"] # all seach fields 
    ordering = ["email"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin) # It connects your custom user model to the admin interface so you can manage users easily.
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.

