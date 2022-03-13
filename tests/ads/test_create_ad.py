import pytest


@pytest.mark.django_db
def test_ads_create(client, user, category):
    response = client.post(
        "/ad/create/",
        {
            "name": "nnnnnnnnnnnnnn",
            "price": 10,
            "description": "test description",
            "is_published": False,
            "author": user.id,
            "category": category.id
        },
        content_type="application/json")

    assert response.status_code == 201
    assert response.data == {
        "id": 2,
        "author": user.id,
        "category": category.id,
        "description": 'test description',
        "image": None,
        "is_published": False,
        "name": "nnnnnnnnnnnnnn",
        "price": 10,
    }
