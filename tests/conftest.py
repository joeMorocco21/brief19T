# pylint: disable=redefined-outer-name
import pytest

from App.app import app as flask_app
from App.apps import classNames as classy


@pytest.fixture
def app():
    yield flask_app



@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def fixture():
    yield 
    assert False 

@pytest.fixture(scope='class')
def classby():
   new_class = classy()
   yield new_class
   #new_class.remove('Hand')
