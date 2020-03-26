from django.shortcuts import render


def budget_view(request):
    return render(
        request, "budget/budget.html", {
            'foo': 'bar',
            'name': 'pepito perez'
        }, content_type = 'text/html'
    )
