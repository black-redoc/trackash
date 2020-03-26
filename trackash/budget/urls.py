from django.urls import path

from trackash.budget.views import budget_view

app_name = "budget"
urlpatterns = [path("home", view=budget_view, name="budget_home")]
