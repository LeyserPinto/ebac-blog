import pytest
from django.urls import reverse

@pytest.fixture
@pytest.mark.urls('classroom.urls')

def test_something(client):
    url = reverse('home')
    assert 'Success!' in client.get(url).content()