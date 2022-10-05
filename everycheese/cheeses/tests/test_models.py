import pytest
from ..models import Cheese

pytestmark = pytest.mark.django_db

def test___str__():
    cheese = Cheese.objects.create(
        name='testcheese',
        description='this is a test description',
        firmness=Cheese.Firmness.SOFT
    )
    assert cheese.__str__() == 'testcheese'
    assert str(cheese) == 'testcheese'