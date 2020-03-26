from django.shortcuts import render
from django.views import View


class DashboardView(View):
    def get(request):
        pass



def budget_view(request):
    return render(
        request, "budget/budget.html", {
            'foo': 'bar',
            'name': 'pepito perez'
        }, content_type = 'text/html'
    )
