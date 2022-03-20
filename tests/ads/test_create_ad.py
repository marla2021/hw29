import pytest


@pytest.mark.django_db
def test_ads_create(client, user, category):
    response = client.post(
        "/ad/create/",
        {
            "name": "test",
            "price": 10,
            "description": "test description",
            "is_published": False,
            "author_id": user.id,
            "category_id": category.id,
        },
        content_type="application/json",
    )

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "name": "test",
        "author_id": user.id,
        "price": 10,
        "description": "test description",
        "is_published": False,
        "category_id": category.id,
    }
