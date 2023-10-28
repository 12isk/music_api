from fastapi.testclient import TestClient
from server import api


client = TestClient(api.app)


def test_get_albums_by_id_13():
    response = client.get("artists/13/albums")

    dic = [{"AlbumId": 18, "ArtistId": 13, "Title": "Body Count"}]
    assert response.status_code == 200
    assert response.json() == dic


def test_get_albums_by_id_0():
    response = client.get("artists/0/albums")

    dic = {"detail": "Albums not found."}
    assert response.status_code == 404
    assert response.json() == dic


def test_get_albums_by_id_999():
    response = client.get("artists/999/albums")

    dic = {"detail": "Albums not found."}
    assert response.status_code == 404
    assert response.json() == dic


def test_get_albums_by_id_1():
    response = client.get("artists/1/albums")

    dic = [
        {"Title": "For Those About To Rock We Salute You", "ArtistId": 1, "AlbumId": 1},
        {"Title": "Let There Be Rock", "ArtistId": 1, "AlbumId": 4},
    ]

    assert response.status_code == 200
    assert response.json() == dic


def test_get_tracks_999():
    response = client.get("albums/999")

    dic = {"detail": "Tracks not found."}
    assert response.status_code == 404
    assert response.json() == dic


def test_get_tracks_0():
    response = client.get("albums/0")

    dic = {"detail": "Tracks not found."}
    assert response.status_code == 404
    assert response.json() == dic


def test_get_tracks_13():
    response = client.get("albums/13")

    dic = [
        {"Name": "Quadrant", "TrackId": 123, "GenreId": 2, "AlbumID": 13},
        {
            "Name": "Snoopy's search-Red baron",
            "TrackId": 124,
            "GenreId": 2,
            "AlbumID": 13,
        },
        {
            "Name": 'Spanish moss-"A sound portrait"-Spanish moss',
            "TrackId": 125,
            "GenreId": 2,
            "AlbumID": 13,
        },
        {"Name": "Moon germs", "TrackId": 126, "GenreId": 2, "AlbumID": 13},
        {"Name": "Stratus", "TrackId": 127, "GenreId": 2, "AlbumID": 13},
        {"Name": "The pleasant pheasant", "TrackId": 128, "GenreId": 2, "AlbumID": 13},
        {"Name": "Solo-Panhandler", "TrackId": 129, "GenreId": 2, "AlbumID": 13},
        {"Name": "Do what cha wanna", "TrackId": 130, "GenreId": 2, "AlbumID": 13},
    ]

    assert response.status_code == 200
    assert response.json() == dic


def test_get_tracks_1():
    response = client.get("albums/1")

    dic = [
        {
            "Name": "For Those About To Rock (We Salute You)",
            "TrackId": 1,
            "GenreId": 1,
            "AlbumID": 1,
        },
        {"Name": "Put The Finger On You", "TrackId": 6, "GenreId": 1, "AlbumID": 1},
        {"Name": "Let's Get It Up", "TrackId": 7, "GenreId": 1, "AlbumID": 1},
        {"Name": "Inject The Venom", "TrackId": 8, "GenreId": 1, "AlbumID": 1},
        {"Name": "Snowballed", "TrackId": 9, "GenreId": 1, "AlbumID": 1},
        {"Name": "Evil Walks", "TrackId": 10, "GenreId": 1, "AlbumID": 1},
        {"Name": "C.O.D.", "TrackId": 11, "GenreId": 1, "AlbumID": 1},
        {"Name": "Breaking The Rules", "TrackId": 12, "GenreId": 1, "AlbumID": 1},
        {"Name": "Night Of The Long Knives", "TrackId": 13, "GenreId": 1, "AlbumID": 1},
        {"Name": "Spellbound", "TrackId": 14, "GenreId": 1, "AlbumID": 1},
    ]

    assert response.status_code == 200
    assert response.json() == dic


def test_get_artist_acdc():
    response = client.get("artists/name/acdc")

    dic = {"detail": "Artist not found."}
    assert response.status_code == 404
    assert response.json() == dic


def test_get_artist_acdc_with_slash():
    response = client.get("artists/name/AC%2fDC")

    dic = {"detail": "Not Found"}
    assert response.status_code == 404
    assert response.json() == dic


def test_get_artist_char_at():
    response = client.get("artists/name/@")

    dic = {"detail": "Artist not found."}
    assert response.status_code == 404
    assert response.json() == dic


def test_get_artist_brown():
    response = client.get("artists/name/brown")

    dic = {
        "artist_name": [
            {"ArtistId": 91, "Name": "James Brown"},
            {"ArtistId": 165, "Name": "Jackson Browne"},
            {"ArtistId": 185, "Name": "Charlie Brown Jr."},
        ]
    }
    assert response.status_code == 200
    assert response.json() == dic


def test_get_artist_mcmiller():
    # obviously i'm conscious this is not an artist
    response = client.get("artists/name/mcmiller")

    dic = {"detail": "Artist not found."}
    assert response.status_code == 404
    assert response.json() == dic


def test_create_genre():
    data = {"title": "Elysium"}
    response = client.post("genres/", params=data)

    dic = {"Success": "Genre Elysium created"}
    assert response.status_code == 200
    assert response.json() == dic
