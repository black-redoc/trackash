from django.urls import path, include

from trackash.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    ProfileUpdateView,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("profile/<str:username>/", view=ProfileUpdateView.as_view(), name="profile"),
]
