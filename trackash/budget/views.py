from django.shortcuts import render
from django.views import View

from .models import Budget


class DashboardView(View):
    budget = Budget.objects.first()
    context = {"budget": budget}

    def get(self, request, *args, **kwargs):
        return render(request, "budget/dashboard.html", self.context)


def budget_view(request):
    return render(
        request,
        "budget/budget.html",
        {"foo": "bar", "name": "pepito perez"},
        content_type="text/html",
    )
