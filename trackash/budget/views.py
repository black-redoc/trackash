from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView

from .models import Budget, Income, Expense
from .forms import IncomeForm, ExpenseForm


class DashboardView(View):
    budget = Budget.objects.first()
    context = {"budget": budget}

    def get(self, request, *args, **kwargs):
        return render(request, "budget/dashboard.html", self.context)


class IncomeCreateView(CreateView):
    model = Income
    form_class = IncomeForm
    success_url = reverse_lazy("budget:dashboard")


class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    success_url = reverse_lazy("budget:dashboard")


def budget_view(request):
    return render(
        request,
        "budget/budget.html",
        {"foo": "bar", "name": "pepito perez"},
        content_type="text/html",
    )
