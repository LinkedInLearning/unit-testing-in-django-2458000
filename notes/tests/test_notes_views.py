import pytest

from django.contrib.auth.models import User

from notes.models import Notes
from .factories import UserFactory

@pytest.fixture
def logged_user(client):
    user = UserFactory()
    client.login(username=user.username, password='password') 
    return user

@pytest.mark.django_db
def test_list_endpoint_returns_user_notes(client, logged_user):
    note = Notes.objects.create(title="a title", text="some text", user=logged_user)
    second_note = Notes.objects.create(title="Another note", text="some text", user=logged_user)

    response = client.get('/smart/notes')
    content = str(response.content)

    assert 200 == response.status_code
    assert "a title" in content
    assert "Another note" in content
    assert 2 == content.count('<h3>')

@pytest.mark.django_db
def test_list_endpoint_only_returns_notes_from_authenticated_user(client, logged_user):
    another_user = UserFactory()
    Notes.objects.create(title="A particular title", text="some text", user=another_user)

    note = Notes.objects.create(title="a title", text="some text", user=logged_user)
    second_note = Notes.objects.create(title="Another note", text="some text", user=logged_user)

    response = client.get('/smart/notes')
    content = str(response.content)

    assert 200 == response.status_code
    assert "a title" in content
    assert "Another note" in content
    assert "A particular title" not in content
    assert 2 == content.count('<h3>')
