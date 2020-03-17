from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _

from .choices import expense_category, income_category


class Extract(models.Model):
    since = models.DateTimeField(_("Since"))
    until = models.DateTimeField(_("Until"))
    month = models.CharField(_("Month"), max_length=12)
    year = models.CharField(_("Year"), max_length=10)
    incomes = JSONField()
    expenses = JSONField()


class Budget(models.Model):
    class Meta:
        verbose_name_plural = _("Budget")

    created_at = models.DateTimeField(
        _("Created At"), auto_now=False, auto_now_add=False
    )
    modiefied_at = models.DateTimeField(_("Modified At"), auto_now=True)
    budget = models.DecimalField(_("Budget"), max_digits=10, decimal_places=2)
    incomes = models.DecimalField(_("Incomes"), max_digits=7, decimal_places=2)
    expenses = models.DecimalField(_("Expenses"), max_digits=7, decimal_places=2)


class Income(models.Model):
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    modiefied_at = models.DateTimeField(_("Modified At"), auto_now=True)
    concept = models.CharField(_("Concept"), max_length=50)
    value = models.CharField(_("Value"), max_length=50)
    category = models.CharField(_("Category"), max_length=50, choices=income_category)


class Expense(models.Model):
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    modiefied_at = models.DateTimeField(_("Modified At"), auto_now=True)
    concept = models.CharField(_("Concept"), max_length=50)
    value = models.CharField(_("Value"), max_length=50)
    category = models.CharField(_("Category"), max_length=50, choices=expense_category)
