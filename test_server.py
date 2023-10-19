from fastapi.testclient import TestClient
from server import api


client = TestClient(api.app)


def test_get_albums_by_id():
    response = client.get("/albums/42")

    dic = [{"AlbumId": 18, "ArtistId": 13, "Title": "Body Count"}]

    assert response.status_code == 200
    assert response.json() == dic


# todo: car not existing
# ac/dict
# 10 test_get_albums_by_id
