import factory

from ads.models import Ad, Category, User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category



class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    birth_date = factory.Faker("date_of_birth", minimum_age=9)
    email = factory.Faker("email", domain="gmail.com")


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad
    name = "nnnnnnnnnnnnnn"
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
    price = 19
    id = factory.Sequence(lambda n: '%s' % n)
