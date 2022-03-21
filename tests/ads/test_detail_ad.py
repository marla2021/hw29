import pytest


@pytest.mark.django_db
def test_detail_ad(client, ad, user_token):
    response = client.get(
        f"/ad/{ad.id}/",
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {user_token}")
    if ad.id:
        assert response.status_code == 200
        assert response.json() == {
        "id": ad.id,
        "is_published": ad.is_published,
        "name": ad.name,
        "price": ad.price,
        "description": ad.description,
        "image": ad.image.url if ad.image else None,
        "author": ad.author_id,
        "category": ad.category_id
        }
    else:
        assert response.status_code == 404