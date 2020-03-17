from django.contrib import admin

from .models import Income, Expense, Budget


"""
form = UserChangeForm
add_form = UserCreationForm
fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
list_display = ["username", "name", "is_superuser"]
search_fields = ["name"]
"""

admin.site.register(Budget)

admin.site.register(Income)

admin.site.register(Expense)
