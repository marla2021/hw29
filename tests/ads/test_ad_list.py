import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_ads_list(client):
    ads_factories = AdFactory.create_batch(10)
    response = client.get("/ad/")
    ads = []
    for ad in ads_factories:
        ads.append({
            "id": ad.id,
            "author": None,
            "name": ad.name,
            "price": ad.price,
        })

    expected_response = {
        "items": ads,
        "num_pages": 1,
        "total": 10,
    }

    assert response.status_code == 200
    assert response.json() == expected_response

