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
        {
            "Name": "Quadrant",
            "AlbumID": 13,
            "Composer": "Billy Cobham",
            "TrackId": 123,
            "Milliseconds": 261851,
        },
        {
            "Name": "Snoopy's search-Red baron",
            "AlbumID": 13,
            "Composer": "Billy Cobham",
            "TrackId": 124,
            "Milliseconds": 456071,
        },
        {
            "Name": 'Spanish moss-"A sound portrait"-Spanish moss',
            "AlbumID": 13,
            "Composer": "Billy Cobham",
            "TrackId": 125,
            "Milliseconds": 248084,
        },
        {
            "Name": "Moon germs",
            "AlbumID": 13,
            "Composer": "Billy Cobham",
            "TrackId": 126,
            "Milliseconds": 294060,
        },
        {
            "Name": "Stratus",
            "AlbumID": 13,
            "Composer": "Billy Cobham",
            "TrackId": 127,
            "Milliseconds": 582086,
        },
        {
            "Name": "The pleasant pheasant",
            "AlbumID": 13,
            "Composer": "Billy Cobham",
            "TrackId": 128,
            "Milliseconds": 318066,
        },
        {
            "Name": "Solo-Panhandler",
            "AlbumID": 13,
            "Composer": "Billy Cobham",
            "TrackId": 129,
            "Milliseconds": 246151,
        },
        {
            "Name": "Do what cha wanna",
            "AlbumID": 13,
            "Composer": "George Duke",
            "TrackId": 130,
            "Milliseconds": 274155,
        },
    ]

    assert response.status_code == 200
    assert response.json() == dic


def test_get_tracks_1():
    response = client.get("albums/1")

    dic = [
        {
            "Composer": "Angus Young, Malcolm Young, Brian Johnson",
            "Name": "For Those About To Rock (We Salute You)",
            "AlbumID": 1,
            "TrackId": 1,
            "Milliseconds": 343719,
        },
        {
            "Composer": "Angus Young, Malcolm Young, Brian Johnson",
            "Name": "Put The Finger On You",
            "AlbumID": 1,
            "TrackId": 6,
            "Milliseconds": 205662,
        },
        {
            "Composer": "Angus Young, Malcolm Young, Brian Johnson",
            "Name": "Let's Get It Up",
            "AlbumID": 1,
            "TrackId": 7,
            "Milliseconds": 233926,
        },
        {
            "Composer": "Angus Young, Malcolm Young, Brian Johnson",
            "Name": "Inject The Venom",
            "AlbumID": 1,
            "TrackId": 8,
            "Milliseconds": 210834,
        },
        {
            "Composer": "Angus Young, Malcolm Young, Brian Johnson",
            "Name": "Snowballed",
            "AlbumID": 1,
            "TrackId": 9,
            "Milliseconds": 203102,
        },
        {
            "Composer": "Angus Young, Malcolm Young, Brian Johnson",
            "Name": "Evil Walks",
            "AlbumID": 1,
            "TrackId": 10,
            "Milliseconds": 263497,
        },
        {
            "Composer": "Angus Young, Malcolm Young, Brian Johnson",
            "Name": "C.O.D.",
            "AlbumID": 1,
            "TrackId": 11,
            "Milliseconds": 199836,
        },
        {
            "Composer": "Angus Young, Malcolm Young, Brian Johnson",
            "Name": "Breaking The Rules",
            "AlbumID": 1,
            "TrackId": 12,
            "Milliseconds": 263288,
        },
        {
            "Composer": "Angus Young, Malcolm Young, Brian Johnson",
            "Name": "Night Of The Long Knives",
            "AlbumID": 1,
            "TrackId": 13,
            "Milliseconds": 205688,
        },
        {
            "Composer": "Angus Young, Malcolm Young, Brian Johnson",
            "Name": "Spellbound",
            "AlbumID": 1,
            "TrackId": 14,
            "Milliseconds": 270863,
        },
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
