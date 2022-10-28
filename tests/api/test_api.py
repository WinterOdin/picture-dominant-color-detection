import pytest


@pytest.mark.django_db
def test_post_api(payload, client):
 
    response_create = client.post("/api/picture/", payload)
    
    data = response_create.data

    assert data["image_large"] is not None
    assert data["dominant_hex"] == "#B52D5D"
    assert data["width"] == "50"



