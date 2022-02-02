from django.contrib import admin
from users.models import User
from basket.admin import BasketAdmin
# Register your models here.

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdmin,)
