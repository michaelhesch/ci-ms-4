from django.urls import path

from . import apps

from .views import (
    ProfileView,
)

app_name = apps.ProfilesConfig.name

urlpatterns = [
    path('<username>/', ProfileView.as_view(), name='profile'),
]
