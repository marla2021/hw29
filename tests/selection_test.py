from typing import List

import pytest

from ads.models import Selection


@pytest.mark.django_db
def test_selection_create(client, user_token, user, ad):
    response = client.post(
        "/selection/create/",
        {
            "name": "test selection",
            "owner": user.id,
            "items": [ad.id]
        },
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {user_token}")
    selection: List[Selection] = Selection.objects.all()
    assert len(selection) == 1

    assert response.status_code == 201
    assert response.data == {"id": selection[0].pk, "name": "test selection", "owner": user.id, "items": [ad.id]}