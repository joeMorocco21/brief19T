
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
    assert b'Radiology Image'in response.data
    assert b'Predictions output'in response.data
    assert b'Built using Pytorch, Flask and Bootstrap.'in response.data
    # pass
    # data = response.data.decode() #Permet de décoder la data dans la requête
    # assert b'Flask User Management Example!'in response.data
    # assert b'Need an account?'in response.data
    # assert b'Existing user?'in response.data
    #assert response.json('hello.html')
    #assert isinstance(response.json, dict)
    #expected = {'index.html'}
    #assert expected == json.loads(response.get_data(as_text=True))


def test_index_bad_http_method(client: FlaskClient, fixture):
    response = client.post('/')
    assert response.status_code == 405
    assert b'Radiology Image' not in response.data
    

def test_upload_text_stream(client: FlaskClient):
    file_name = "fake-text-stream.txt"
    data = {
        'image': (io.BytesIO(b"some initial text data"), file_name)
    }
    response = client.post('/storImages', data=data)
    assert response.status_code == 400


def test_upload_textfile(client):
    file = "/Users/badewaaderogba/hello_project/Flask_image/App/random-file.txt"
    data = {
        'image': (open(file, 'rb'), file)
    }
    response = client.post('/storImages', data=data)
    assert response.status_code == 400

@pytest.mark.xfail(sys.platform == 'linux', reason='window behaviour')    
def test_upload_image_stream(client: FlaskClient):
    image_name = "fake-image-stream.jpg"
    data = {
        'file': (io.BytesIO(b"some random data"), image_name)
    }
    response = client.post('/storImages', data=data)
    assert response.status_code == 400
    assert response.json['predict'] == image_name
    assert response.json.get('success')
    assert False 
    
def test_upload_image_file(client: FlaskClient):
    image = "pizza-cat.jpeg"
    data = {
        'image': (open(image, 'rb'), image)
    }
    response = client.post('/storImages', data=data)
    assert response.status_code == 200
    #assert response.json['message'] == image
    assert response.json['application/json'] == image
    assert response.json.get('success')