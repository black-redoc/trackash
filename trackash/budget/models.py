from calendar import monthrange

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
    def set_incomes(income_list):
        # Transforms a list of Income model in a list of dict
        ls = {}
        for inc in income_list:
            ls.update(
                {
                    inc.id: {
                        "id": inc.id,
                        "created_at": inc.created_at,
                        "modified_at": inc.modified_at,
                        "concept": inc.concept,
                        "value": inc.value,
                        "category": inc.category,
                    }
                }
            )
        return ls

    @staticmethod
    def set_expenses(expense_list):
        # Transforms a list of Expense model in a list of dict
        ls = {}
        for exp in expense_list:
            ls.update(
                {
                    exp.id: {
                        "id": exp.id,
                        "created_at": ex.created_at,
                        "modified_at": ex.modified_at,
                        "concept": exp.concept,
                        "value": exp.value,
                        "category": inc.category,
                    }
                }
            )
        return ls

    @staticmethod
    def delete_income(pk, sc):
        """
        delete_income() deletes the income from the Extract model

        Parameters:
        pk: int Is the primary key of the Income
        sc: datetime Is the filter parameter for 
            find the respective Extract
        """
        del_income = Extract.objects.filter(since=sc).first()
        if del_income:
            del del_income.incomes[pk]
            del_income.save()

    @staticmethod
    def delete_expense(pk, sc):
        """
        delete_expense() deletes the income from the Extract model

        Parameters:
        pk: int Is the primary key of the Expense
        sc: datetime Is the filter parameter for 
            find the respective Extract
        """
        del_expense = Extract.objects.filter(since=sc).first()
        if del_expense:
            del del_expense.expenses[pk]
            del_expense.save()


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
