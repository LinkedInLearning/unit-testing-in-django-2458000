import pytest

from django.contrib.auth.models import User

def test_home_endpoint_returns_a_welcome_page(client):
    response = client.get(path='/')
    assert response.status_code == 200
    assert 'Welcome to SmartNotes!' in str(response.content)

def test_signup_endpoint_returns_from_for_unauthenticated_user(client):
    response = client.get(path='/signup')
    assert response.status_code == 200
    assert 'Enter the same password as before, for verification' in str(response.content)

@pytest.mark.django_db
def test_signup_endpoint_redirects_authenticated_user(client):
    '''
      When a user is authenticated and try to access the 
      signup page, they are redirected to the list of their notes.
    '''
    user = User.objects.create_user('Clara', 'clara@test.com', 'password')
    client.login(username=user.username, password='password')
    assert user.is_authenticated

    response = client.get(path='/signup', follow=True)
    print(type(response))
    assert response.status_code == 200
    assert 'notes/notes_list.html' in response.template_name