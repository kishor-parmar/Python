# cd ~/Library/Mobile\ Documents/com~apple~CloudDocs/Documents/Respositories
# cd 3\ -\ Testing
# pytest tests/test_service.py -v
#

import requests

import pytest

import source.service as service

import unittest.mock as mock


@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(1)

    assert user_name == "Mocked Alice"


@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    mock_response.return_value = mock_response
    data = service.get_users()

    assert data == {"id": 1, "name": "John Doe"}
