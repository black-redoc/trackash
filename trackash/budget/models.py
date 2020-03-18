from calendar import monthrange

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _

from .choices import expense_category, income_category


class Extract(models.Model):
    since = models.DateTimeField(_("Since"))
    until = models.DateTimeField(_("Until"))
    month = models.CharField(_("Month"), max_length=12)
    amount = models.DecimalField(_("Amount"), max_digits=10, decimal_places=2)
    year = models.CharField(_("Year"), max_length=4)

    @property
    def get_incomes(self):
        # Get the month Incomes queryset
        return Income.objects.filter(
            creatd_at__gte=self.since, created_at__lte=self.until
        )

    @property
    def get_expenses(self):
        # Get the month Expenses queryset
        return Expense.objects.filter(
            created_at__gte=self.since, created_at__lte=self.until
        )

    @staticmethod
    def monthly_extract(today):
        """ Create the monthly extract """
        from calendar import monthrange
        from functools import reduce

        last_day = monthrange(year=today.year, month=today.month - 1)[1]
        local_month = today.strftime("%B")

        local_since = today.replace(
            month=today.month - 1, day=1, hour=0, minute=0, second=0, microsecond=0
        )

        local_until = today.replace(
            month=today.month - 1,
            day=last_day,
            hour=23,
            minute=59,
            second=59,
            microsecond=999999,
        )

        local_incomes = reduce(
            lambda x, y: x.value + y.value,
            Income.objects.filter(
                created_at__gte=local_since, created_at__lte=local_until
            ),
        )

        local_expenses = reduce(
            lambda x, y: x.value + y.value,
            Expense.objects.filter(
                created_at__gte=local_since, created_at__lte=local_until
            ),
        )

        Extract.objects.create(
            since=local_since,
            until=local_until,
            month=local_month,
            year=today.year,
            amount=local_incomes - local_expenses,
        )


class Budget(models.Model):
    class Meta:
        verbose_name_plural = _("Budget")

    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified At"), auto_now=True)
    budget = models.DecimalField(_("Budget"), max_digits=11, decimal_places=2)
    incomes = models.DecimalField(_("Incomes"), max_digits=11, decimal_places=2)
    expenses = models.DecimalField(_("Expenses"), max_digits=11, decimal_places=2)


class Income(models.Model):
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified At"), auto_now=True)
    concept = models.CharField(_("Concept"), max_length=50)
    value = models.CharField(_("Value"), max_length=50)
    category = models.CharField(_("Category"), max_length=50, choices=income_category)


class Expense(models.Model):
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified At"), auto_now=True)
    concept = models.CharField(_("Concept"), max_length=50)
    value = models.CharField(_("Value"), max_length=50)
    category = models.CharField(_("Category"), max_length=50, choices=expense_category)
