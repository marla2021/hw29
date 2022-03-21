import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_ads_list(client, ad, user_token):
    response = client.get("/ad/")
    ads_factories = AdFactory.create_batch(1)
    ads = []
    i=3
    for ad in ads_factories:
        ads.append({
            "id": i,
            "author": None,
            "name": ad.name,
            "price": ad.price,
        })
        i+=1

    expected_response = {
        "items": ads,
        "num_pages": 1,
        "total": 1,
    }

    assert response.status_code == 200
    assert response.json() == expected_response

