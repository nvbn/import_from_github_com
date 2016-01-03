def test_import_module():
    from github_com.kennethreitz import requests

    assert requests.get('https://github.com').status_code == 200


def test_import_from_module():
    from github_com.kennethreitz.requests import get

    assert get('https://github.com').status_code == 200
