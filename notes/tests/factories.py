import factory
from factory import fuzzy

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from notes.models import Notes

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user_{n:04}")
    email = factory.LazyAttribute(lambda user: f"{user.username}@example.com")
    password = factory.LazyFunction(lambda: make_password('password'))

class NoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Notes
    
    title = fuzzy.FuzzyText(length=20)
    text = fuzzy.FuzzyText(length=200)
    user = factory.SubFactory(UserFactory)
