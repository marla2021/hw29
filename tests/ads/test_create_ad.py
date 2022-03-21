from typing import List

import pytest

from ads.models import Ad


@pytest.mark.django_db
def test_ads_create(client, user, category):
    assert not Ad.objects.all()
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
    ads: List[Ad] = Ad.objects.all()
    assert len(ads) == 1

    assert response.status_code == 201
    assert response.json() == {
        "id": ads[0].pk,
        "name": "test",
        "author_id": user.id,
        "price": 10,
        "description": "test description",
        "is_published": False,
        "category_id": category.id,
    }
