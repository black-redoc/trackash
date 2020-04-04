from django.urls import path

from trackash.budget.views import budget_view, DashboardView

app_name = "budget"
urlpatterns = [
    path("dashboard", view=DashboardView.as_view(), name="dashboard"),
    path("home", view=budget_view, name="home"),
]
