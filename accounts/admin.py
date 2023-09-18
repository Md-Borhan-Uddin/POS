from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import User
from .forms import CustomUserChangeForm, AdminCreationForm
# Register your models here.



class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = AdminCreationForm
    model = User

    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)

    fieldsets = (
        ('Account Info', {"fields": ("email", "password")}),
        ('User Info',{'fields':('first_name','last_name','dob')}),
        ("Permissions", {"fields": ("is_superuser","is_staff", "is_active", "groups", "user_permissions")}),
        ('Timestamp',{'fields':('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", 
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    readonly_fields  =('password',)


admin.site.register(User, CustomUserAdmin)

