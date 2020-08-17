import pytest
from django.template.defaultfilters import slugify
from everycheese.users.tests.factories import UserFactory

import factory
import factory.fuzzy
from ..models import Cheese


class CheeseFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    firmness = factory.fuzzy.FuzzyChoice([x[0] for x in Cheese.Firmness.choices])
    country_of_origin = factory.Faker('country_code')
    creator = factory.SubFactory(UserFactory)

    class Meta:
        model = Cheese


@pytest.fixture
def cheese():
    return CheeseFactory()
