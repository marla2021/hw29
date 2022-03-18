from datetime import date

import pytest
from faker import Faker


@pytest.fixture()
@pytest.mark.django_db
def user_token(client, django_user_model):
    username = "username"
    password = "password"


    django_user_model.objects.create_user(username=username, password=password, role="hr",
                                          birth_date = date(1970, 1, 1), email= "test@test.ru")
    response = client.post("/user/token/", {"username": username, "password": password}, format='json')

    return response.data["access"]
