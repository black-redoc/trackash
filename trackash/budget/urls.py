from django.urls import path

from trackash.budget.views import budget_view, DashboardView, IncomeCreateView

app_name = "budget"
urlpatterns = [
    path("dashboard", view=DashboardView.as_view(), name="dashboard"),
    path("income/", view=IncomeCreateView.as_view(), name="income"),
    path("home", view=budget_view, name="home"),
]
