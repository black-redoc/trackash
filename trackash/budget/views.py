from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView

from .models import Budget, Income


class DashboardView(View):
    budget = Budget.objects.first()
    context = {"budget": budget}

    def get(self, request, *args, **kwargs):
        return render(request, "budget/dashboard.html", self.context)


class IncomeCreateView(CreateView):
    model = Income
    fields = ("concept", "value", "category")
    
    def get_success_url(self):
        return reverse_lazy("budget:dashboard")

def budget_view(request):
    return render(
        request,
        "budget/budget.html",
        {"foo": "bar", "name": "pepito perez"},
        content_type="text/html",
    )
