from django.urls import path

from apps.auth.views import UserView

urlpatterns = [
    path('', UserView.as_view())
]
