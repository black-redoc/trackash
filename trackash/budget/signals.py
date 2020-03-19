from decimal import Decimal

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Income, Expense, Budget


@receiver(post_save, sender=Income, dispatch_uid="trackash.budget.income.post_save")
def post_save_income(sender, instance, *args, **kwargs):
    """  Add income value for budget """
    try:
        budget_ = Budget.objects.get(id=1)
        budget_.incomes += Decimal(str(instance.value))
        budget_.budget += Decimal(str(instance.value))
        budget_.save()
    except:
        Budget.objects.create(
            budget=Decimal(str(instance.value)),
            incomes=Decimal(str(instance.value)),
            expenses=Decimal(),
        )


@receiver(post_save, sender=Expense, dispatch_uid="trackash.budget.expense.post_save")
def post_save_expense(sender, instance, *args, **kwargs):
    """ Subs expense value for budget """
    try:
        budget_ = Budget.objects.get(id=1)
        budget_.expenses += Decimal(str(instance.value))
        budget_.budget -= Decimal(str(instance.value))
        budget_.save()
    except:
        Budget.objects.create(
            budget=Decimal(str(-instance.value)),
            incomes=Decimal(),
            expenses=Decimal(str(instance.value)),
        )
