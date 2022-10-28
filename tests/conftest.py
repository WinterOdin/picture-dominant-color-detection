import pytest 
from io import BytesIO
#from io import StringIO
from PIL import Image
from api.models import Pictures
from django.core.files.base import File
from rest_framework.test import APIClient


def get_image_file(name='test.png', ext='png', size=(50, 50), color=(181, 45, 93)):
    file_obj = BytesIO()
    image = Image.new("RGB", size=size, color=color)
    image.save(file_obj, ext)
    file_obj.seek(0)
    return File(file_obj, name=name)


@pytest.fixture
def payload():

    data = dict(
        title = "test_title",
        album_id = "test_id",
        image = get_image_file()
    )
    return data 

@pytest.fixture
def client():
    return APIClient()