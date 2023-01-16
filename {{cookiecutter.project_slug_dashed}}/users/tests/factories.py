import factory
from factory import Faker, post_generation

from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    username = Faker("user_name")
    email = Faker("email")

    @post_generation
    def password(self, create, extracted, **kwargs):
        self.set_password("password")

    class Meta:
        model = User
        django_get_or_create = ["username"]
