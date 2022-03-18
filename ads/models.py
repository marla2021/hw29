from datetime import date, datetime

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from rest_framework.exceptions import ValidationError



class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name

USER_MIN_AGE = 9

def check_birth_date(value: date):
    delta = relativedelta(date.today(), value).years
    if delta < USER_MIN_AGE:
        raise ValidationError(
            'You are too small',
        )

class User(AbstractUser):
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLES = [
        ("member", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Админ"),
    ]

    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLES, default=MEMBER)
    location = models.ManyToManyField(Location)
    birth_date = models.DateField(validators=[check_birth_date])
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username

    @property
    def age(self):
        now: date = datetime.utcnow().date()
        return relativedelta(now, self.birth_date).years


class Category(models.Model):
    slug = models.CharField(max_length=10,validators=[MinLengthValidator(5)],blank=True, null=True)
    name = models.CharField(max_length=100)


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to="upload_image/", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)