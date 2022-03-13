import factory

from ads.models import Ad, Category, User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    slug = factory.Faker("color")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")

class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad
    name = "nnnnnnnnnnnnnn"
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
    price = 19
