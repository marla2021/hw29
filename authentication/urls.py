from django.urls import path

from authentication.views import UserAuthCreateView

urlpatterns = [
    path('create/', UserAuthCreateView.as_view()),
]