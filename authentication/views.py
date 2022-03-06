from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from ads.models import User
from authentication.serializers import UserAuthSerializer


class UserAuthCreateView(CreateAPIView):
    model = User
    serializer_class = UserAuthSerializer