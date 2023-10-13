import pytest
from server import api


def test_get_albums_by_id():
    assert(api.get_album_by_id(1))
