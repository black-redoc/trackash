from django.shortcuts import render
from django.views import View

from .models import Budget


class DashboardView(View):
    queryset = Budget.objects.filter().first()
    context = {"queryset": queryset}

    def get(request):
        return render(request, "budget/dashboard.html", context)


def budget_view(request):
    return render(
        request,
        "budget/budget.html",
        {"foo": "bar", "name": "pepito perez"},
        content_type="text/html",
    )
