from django.urls import path
from .views import ProfileRetrieveAPIView, ProfileUpdateAPIView

app_name = "api-profile"
urlpatterns = [
    path(
        "profile/<int:pk>/", ProfileRetrieveAPIView.as_view(), name="profile-retrieve"
    ),
    path(
        "profile/update/<int:pk>/",
        ProfileUpdateAPIView.as_view(),
        name="profile-update",
    ),
]
