from django.contrib import admin

from .models import Income, Expense, Budget, Extract

admin.site.register(Budget)


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ("created_at", "concept", "value", "category")


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("created_at", "concept", "value", "category")


@admin.register(Extract)
class ExtractAdmin(admin.ModelAdmin):
    list_display = ("since", "until", "month", "year")
