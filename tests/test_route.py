import json
import sys
import pytest
from io import BytesIO
import io
from io import StringIO
from flask.testing import FlaskClient



#from App.views import index # Flask instance of the API
#app = Flask(__name__, template_folder='templates')
# @pytest.mark.xfail(strict=True)
# pass
#@pytest.mark.parametrize("app, client")
def test_index(app, client: FlaskClient):
    del app
    response = client.get('/')
    assert response.status_code == 200
    assert b'Result of Prediction'in response.data
    assert b'Upload'in response.data
    assert b'Image'in response.data
    # pass
    # data = response.data.decode() #Permet de décoder la data dans la requête
    # assert b'Flask User Management Example!'in response.data
    # assert b'Need an account?'in response.data
    # assert b'Existing user?'in response.data
    #assert response.json('hello.html')
    #assert isinstance(response.json, dict)
    #expected = {'index.html'}
    #assert expected == json.loads(response.get_data(as_text=True))


def test_index_bad_http_method(client: FlaskClient):
    response = client.post('/')
    assert response.status_code == 405
    assert b'Radiology Image' not in response.data