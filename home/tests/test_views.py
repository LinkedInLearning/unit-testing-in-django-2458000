import pytest

from django.contrib.auth.models import User

def test_home_view(client):
    response = client.get(path='/')
    assert response.status_code == 200
    assert 'Welcome to SmartNotes!' in str(response.content)

def test_signup_get(client):
    response = client.get(path='/signup')
    assert response.status_code == 200
    assert 'Enter the same password as before, for verification' in str(response.content)

@pytest.mark.django_db
def test_signup_authenticated(client):
    user = User.objects.create_user('Clara', 'clara@test.com', 'password')
    client.login(username=user.username, password='password')
    assert user.is_authenticated

    response = client.get(path='/signup', follow=True)
    print(type(response))
    assert response.status_code == 200
    assert 'notes/notes_list.html' in response.template_name