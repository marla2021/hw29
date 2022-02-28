from rest_framework import serializers

from ads.models import User, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field="name"
    )

    class Meta:
        model = User
        exclude = ["password"]


class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        many=True,
        slug_field="name"
    )

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop("location")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for location in self._location:
            obj, _ = Location.objects.get_or_create(name=location)
            user.location.add(obj)

        return user

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}


class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        queryset=Location.objects.all(),
        many=True,
        slug_field="name"
    )

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop("location")
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        for location in self._location:
            obj, _ = Location.objects.get_or_create(name=location)
            user.location.add(obj)

        return user

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]