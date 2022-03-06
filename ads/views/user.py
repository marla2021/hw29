from django.db.models import Count, Q
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


from ads.models import User
from ads.serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer, \
    UserDeleteSerializer


class UserView(ListAPIView):
    queryset = User.objects.all().annotate(ads=Count('ad', filter=Q(ad__is_published=True)))
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer
