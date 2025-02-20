import factory
from django.contrib.auth import get_user_model
from netlify_movies.models import Netflix

User = get_user_model()

class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Netflix

    movie_name = factory.Faker('sentence', nb_words=3)
    category = factory.Faker('word')
    description = factory.Faker('text', max_nb_chars=100)
    year_released = factory.Faker('year')
    director = factory.Faker('name')
    rating = factory.Faker('pyfloat', left_digits=1, right_digits=1, positive=True)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: f"user{n}@test.com")
    password = factory.PostGenerationMethodCall("set_password", "testpassword")
    is_staff = False